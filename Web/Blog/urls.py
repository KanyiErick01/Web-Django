from django.urls import path
from .import views 
from .views import PostView,BlogView

urlpatterns = [
    path('',views.index,name=" "),

    path('loginPage',views.loginPage, name='loginPage'),

    path('signup',views.sign_up,name='signup'),

    path('logout',views.logout,name='signup'),

    path("blog", PostView.as_view(), name="blog"),

    path("post/<int:pk>/", BlogView.as_view(), name="blog_detail"),
    
]