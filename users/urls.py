from django.urls import path
from users import views
urlpatterns=[
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('me/profile',views.UpdateProfileView.as_view(),name='update_profile'),
    path('<str:username>',views.UserDetailView.as_view(),name='detail'),
]