from django.urls import path
from Point import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('category/',views.cat,name="category"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('score/',views.score,name="score"),
    path('<str:cat>/',views.viewCat,name="viewCat"),
    path('<str:cat>/quiz/',views.quiz,name="quiz"),
]