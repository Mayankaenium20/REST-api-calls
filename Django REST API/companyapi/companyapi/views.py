from django.http import JsonResponse

def home_page(request):
    print("HOME PAGE RERQUESTED!")

    friends = ['a', 23, True, None, "dksad", 2+2, 232.4, (2,3)]
    return JsonResponse(friends, safe = False)