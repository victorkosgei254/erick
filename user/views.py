from django.shortcuts import render
from django.views import View
# Create your views here.

class HomePage(View):
    def get(self,request):
        return render('user/index.html')
