from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:post_id>', views.post, name='post'),
    path('sobre',views.sobre, name='sobre'),
    path('form', views.form, name='form'),
    path('create', views.create, name='create'),
    path('update/<int:id>', views.update_post, name='update_post'),
    path('delete/<int:id>', views.delete_post, name='delete_post'),

]