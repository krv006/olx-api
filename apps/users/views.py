from django.http import HttpResponse


def profile(request):
    return HttpResponse("This is the User Profile Page!")
