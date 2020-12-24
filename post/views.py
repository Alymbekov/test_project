from django.shortcuts import render
import post.models

# import post.parser
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("<h1> Hello Django</h1>")

# def index(request):
#     informations = post.parser.main().items()
#     informations = dict(informations)
#     full_name = informations.get('full_name')
#     avatar = informations.get('avatar')
#     print(full_name)
#     print(avatar)
#     lists = [x for x in range(1, 100)]
#     names = ['John', 'Raychel', 'Jane', 'Peter']
#     return render(request, 'index.html', locals())
#
#
def index(request):
    lists = [x for x in range(1, 100)]
    names = ['John', 'Raychel', 'Jane', 'Peter']
    return render(request, 'index.html', locals())

def get_posts(request):
    object_list = post.models.Post.objects.all().only('id', 'title')
    """SELECT * FROM post_post"""
    # post.models.Post.objects.
    # hello = object_list.get(pk=5)
    # print(hello.rating_set.all())
    # print("hello")
    return render(request, 'posts.html', locals())

