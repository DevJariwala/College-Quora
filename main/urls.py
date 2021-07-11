from django.urls import path
from . import views
urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('question/<int:id>',views.questionPage,name="question"),
    path('new-question',views.newQuestionPage,name="new-question"),
    path('delete/<int:id>',views.deleteQuestion,name="delete-question"),
    path('search',views.search,name="search"),
    # path('signup/',views.signUpPage,name="signUp"),
]
