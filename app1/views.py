from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def main(request):
    return render(request, 'app1/main.html')

def create(request):
    if request =='POST':
        pass
    else:
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'app1/create.html', context)