from django.urls import path,include

from user.views import HomePage

urlpatterns=[
    path('',HomePage.as_view(),name="home"),
]