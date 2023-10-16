from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return render(request, 'blog/index.html')
    return render(request, 'blog/index.html', {
        'title' : 'My Blog',
        # 'content' : 'Hello, this is my blog'
        'content' : [
            {
                'id' : 1,
                'title' : 'First Post',
                'content' : 'Hello, This is my First Post'
            },
            {
                'id': 2,
                'title': 'Second Post',
                'content': 'Hello, This is my Second Post'
            },
            {
                'id': 3,
                'title': 'Third Post',
                'content': 'Hello, This is my Third Post'
            }
        ]
    })
