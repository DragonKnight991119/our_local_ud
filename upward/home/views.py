from django.http import HttpResponse
from django.template import loader
# Create your views here.

def home(req):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
