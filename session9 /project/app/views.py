from django.shortcuts import render, redirect
from .models import Article
from .models import Post

def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts' : posts})

def count (request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(' ',''))

    return render(request, 'result.html', 
        {'text': text,'total_len': total_len,'no_blank_len': no_blank_len})

def info(request):
    return render(request,'info.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def new(request):
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')
    

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article': article})

def update(request,	post_pk):
    post= Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        updated_post =Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail',post_pk)
    
    return render(request,'update.html',{'post':post})

def delete(request,	post_pk):
    post= Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home') 
