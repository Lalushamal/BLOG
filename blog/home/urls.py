from django.urls import path
from . import views


urlpatterns =[ 
    path('',views.index,name='index'),
    path('blog/<int:post_id>/',views.blog, name='blog'),
    path('delete/<int:post_id>/',views.delete, name='delete'),
    path('create',views.create,name='create'),
    path('update/<int:post_id>/',views.update, name='update'),
    path('register',views.register, name='register'),
]