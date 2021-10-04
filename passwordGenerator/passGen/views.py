from django.shortcuts import render, redirect
from django.views.generic.base import View
from .password import PasswordGen
from .models import Password

class IndexView(View):

    def index(request):
        latestPswd = Password.objects.last()
        return render(request, 'passGen/index.html', {'password': latestPswd})

    def generate(request):
        pswd = PasswordGen(10)
        db = Password()
        db.password = pswd.generate()
        db.save()
        return redirect('/')

