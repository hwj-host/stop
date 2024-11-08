from django.urls import path
from . import views
urlpatterns = [
    path("bookhome",views.bookhome,name='bookhome'),
    path('<int:book_id>', views.bookdetail, name='bookdetail'),
    path('<int:movie_id>/createmoviereview', views.createmoviereview, name='createmoviereview'),
    path('review/<int:review_id>', views.updatemoviereview, name='updatemoviereview'),
    path('review/<int:review_id>/delete', views.deletemoviereview, name='deletemoviereview'),

]