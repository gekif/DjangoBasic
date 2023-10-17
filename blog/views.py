from django.shortcuts import render,redirect
from blog import models, forms
from django.http import HttpResponse, Http404


def index(request):
    return render(request, 'blog/index.html', {
        'title': 'My Blog',
        'content': models.Post.objects.all()
    })


def detail(request, id):
    try:
        model = models.Post.objects.get(id=id)
    except Exception:
        raise Http404()

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog-detail', id=id)

    else:
        form = forms.CommentForm({'post': model})

    return render(request, 'blog/detail.html', {
        'title': model.title,
        'model': model,
        'form': form
    })
