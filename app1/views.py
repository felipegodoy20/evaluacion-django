from django.http import HttpResponse

# Create your views here.
def vista1(request):
    return HttpResponse("<h1>App 1 - Vista 1</h1><p>Vista principal creada.</p>")

def vista2(request):
    return HttpResponse("<h1>App 1 - Vista 2</h1><p>Vista secundaria creada.</p>")
