from django.http import HttpResponse

def profile(request):
    return HttpResponse("Страница пользователя")
