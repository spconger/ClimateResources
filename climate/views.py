from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    topics=Topic.objects.all()
    return render(request,'climate/index.html',{'topics': topics})