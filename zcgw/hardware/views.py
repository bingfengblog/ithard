from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    duan = 'welcome to django'
    return render_to_response('hardware/index.html',{'word':duan})


