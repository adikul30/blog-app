from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name = 'index'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('new/', views.new, name='new'),
    path('signup/', views.signUp, name='signUp'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('signin/', views.signIn, name='signIn'),
    path('updateblog/<int:blog_id>/', views.updateBlog, name='updateBlog'),
    path('deleteblog/<int:blog_id>/', views.deleteBlog, name='deleteBlog'),

]