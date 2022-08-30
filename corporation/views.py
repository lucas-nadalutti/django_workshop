from django.http import HttpResponse

from .models import Corporation

def index(request):
    result = ""
    for corporation in Corporation.objects.all():
        result += f"{corporation.legal_name} -"
    return HttpResponse(result)
