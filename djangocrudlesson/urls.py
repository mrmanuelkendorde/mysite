from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender), # link for listing genders
    path('gender/create', views.create_gender), # link for creating gender
    path('gender/store', views.store_gender), # link for storing gender
    path('gender/show/<int:gender_id>', views.show_gender), # link for showing gender
    path('gender/edit/<int:gender_id>', views.edit_gender), # link for editing gender
    path('gender/update/<int:gender_id>', views.update_gender), # link for updating gender
    path('gender/delete/<int:gender_id>', views.delete_gender), # link for deleting gender
    path('gender/destroy/<int:gender_id>', views.destroy_gender), # link for destroying gender

    path('users', views.index_user), # link for listing user
    path('users/create', views.create_user), # link for creating user
    path('users/store', views.store_user), # link for storing user
    path('users/delete/<int:user_id>', views.delete_user), # link for showing user
    path('users/destroy/<int:user_id>', views.destroy_user), # link for editing user
    path('users/show/<int:user_id>', views.show_user), # link for updating user
    path('users/edit/<int:user_id>', views.edit_user), # link for deleting user
    path('users/update/<int:user_id>', views.update_user), # link for destroying user
]
