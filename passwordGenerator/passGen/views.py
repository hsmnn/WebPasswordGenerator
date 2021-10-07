from django.shortcuts import render, redirect
from django.views.generic.base import View
from .password import PasswordGen
from .forms import PassForm

class IndexView(View):

    def index(request):
        context = {}
        if (request.session.get('password') != ""):
            context['password'] = request.session.get('password')
        if (request.session.get('length') != None):
            context['form'] = PassForm(initial = {'length': request.session.get('length')})
        else:
            context['form'] = PassForm()
        return render(request, 'passGen/index.html', context)

    def generate(request):
        length = 0
        form = PassForm(request.POST or None)
        if request.POST and form.is_valid():
            length = form.cleaned_data.get("length")
        request.session['password'] = PasswordGen(length).generate()
        request.session['length'] = length
        return redirect('/')
