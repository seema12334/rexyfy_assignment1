from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.pplloginview.as_view(),name='loginpage'),
    path('logout/',LogoutView.as_view(next_page='loginpage'),name='logoutpage'),

    path('welcome/',views.taskviews.as_view(),name='taskviews'),
    path('addtask/',views.taskcreate.as_view(),name='addtask'),
    path('edittask/<int:pk>/',views.taskedit.as_view(),name='edittask'),
    path('deletetask/<int:pk>',views.taskdelete.as_view(),name='deletetask'),

]