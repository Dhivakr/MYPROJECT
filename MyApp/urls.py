from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login_page/',views.login_page,name="login_page"),
    path('logout_page/',views.logout_page,name="logout_page"),
    path('dhashboard/',views.dhashboard,name='dhashboard'),
    path('create_task/',views.create_task,name='create_task'),
    path('view_task/',views.view_task,name='view_task'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),
    path('item/<int:pk>/update/',views.update, name="update"),
    path('detail/<int:pk>/',views.detail_view, name='detail_view'),    
]