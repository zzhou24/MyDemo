from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),   # 注意这个views.index不加括号
    path('users', views.indexUsers, name = 'indexusers' ),
    path('users/add', views.addUsers, name = 'addusers' ),
    path('users/insert', views.insertUsers, name = 'insertusers' ),
    path('users/del/<int:uid>', views.delUsers, name = 'delusers' ),
    path('users/edit/<int:uid>', views.editUsers, name = 'editusers' ),
    path('users/update', views.updateUsers, name = 'updateusers' ),

]
