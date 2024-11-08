from django.shortcuts import render, redirect
from .models import Book, Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 1)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)
    return render(request, 'bookhome.html',
                  {'searchTerm':searchTerm, 'books':books})
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'bookdetail.html', {'book': book, 'reviews':reviews})
@login_required
def createmoviereview(request, movie_id):
    movie = get_object_or_404(Book, pk=movie_id)
    if request.method == 'GET' :
        return render(request, 'createmoviereview.html' ,
        {'form':ReviewForm , 'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = movie
            newReview.save()
            return redirect('moviedetail',newReview.movie.id)
        except ValueError:
            return render(request,'createmoviereview.html', {'form':ReviewForm, 'error':'非法数据'})
@login_required
def updatemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatemoviereview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('moviedetail', review.movie.id)
        except ValueError:
            return render(request, 'updatemoviereview.html', {'review':review, 'form':form, 'error':'提交非法数据'})
@login_required
def deletemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('moviedetail', review.book.id)