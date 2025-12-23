from django.urls import path
from .import views 
from .views import PostView,BlogView

urlpatterns = [
  path('',views.index,name=" "),

  path('signup',views.signUp,name="signup"),

  path('loginPage',views.loginPage,name="loginPage"),

  path('logout',views.logoutuser,name="logout"),

  path("blog", PostView.as_view(), name="blog"),

  path("post/<int:pk>/", BlogView.as_view(), name="blog_detail"),
    
]