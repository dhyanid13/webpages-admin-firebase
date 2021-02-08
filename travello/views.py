from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.img='destination_5.jpg'
    dest1.desc = 'City that never sleeps'
    dest1.name='Mumbai'
    dest1.price=700
    
    dest2=Destination()
    dest2.img='destination_2.jpg'
    dest2.desc = 'Truely Asia'
    dest2.name='Malayaisa'
    dest2.price=700
    
    
    dest3=Destination()
    dest3.name='SFO'
    dest3.img='destination_3.jpg'
    dest3.desc='ONCE you visit your heart will stay here for lifetime'
    dest3.price=1000
    
    dests=[dest1,dest2,dest3]
    
    return render(request,'index.html',{'dests':dests})
