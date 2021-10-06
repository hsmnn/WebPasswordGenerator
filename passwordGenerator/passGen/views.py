from django.shortcuts import render, redirect
from django.views.generic.base import View
from .password import PasswordGen
from .models import Password
from .forms import PassForm

class IndexView(View):

    def index(request):
        latestPswd = Password.objects.last()
        context = {
            'password': latestPswd,
            'form' : PassForm(),
        }
        return render(request, 'passGen/index.html', context)

    def generate(request):
        length = 0
        pswd = ""
        form = PassForm(request.POST or None)
        if request.POST and form.is_valid():
            length = form.cleaned_data.get("length")
        print(length)
        db = Password()
        pswd = PasswordGen(length)
        db.password = pswd.generate()
        db.save()
        return redirect('/')
