from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .forms import PostForm
from .models import Post

def index(request):
    posts = Post.objects.all()

    dados = {
        'posts': posts
    }
    return render(request, 'index.html', dados)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post_a_exibir = {
        'post': post
    }
    return render(request, 'post.html', post_a_exibir)

def sobre(request):
    return render(request, 'sobre.html')

def form(request):
    data = {}
    data['form'] = PostForm()
    return render(request, 'form.html', data)

def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'form.html', {'form': form})

def update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'editar.html', {'form': form, 'post': post})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'delete-confirmacao.html', {'form': form, 'post': post})

# def search(request):
#     if request.method == 'GET': # this will be GET now
#         post_name =  request.GET.get('search') # do some research what it does
#         try:
#             status = Post.objects.filter(postagem_titulo__icontains=post_name) # filter returns a list so you might consider skip except part
#         return render(request,"index.html",{"post":status})
#     else:
#         return render(request,"index.html",{})
