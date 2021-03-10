from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎光临 林本伟先生！")
