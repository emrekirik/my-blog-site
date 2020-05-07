from django.shortcuts import render
from .models import Post
from django.utils import timezone





def Home(request):
    context = dict()
    context['posts'] = Post.objects.filter(
    pub_date__lte=timezone.now(),
    
    ).exclude(cover_image = '').order_by('pub_date')
    return render(request, 'blog/home.html', context)

def Detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post' : post,
    }

    return render(request, 'blog/detail.html', context)