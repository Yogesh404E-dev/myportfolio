from django.shortcuts import render
from django.http import HttpResponse
from .models import servises
# Create your views here.

def index(request):
    servis1 = servises() 
    servis1.name = 'Web Development'
    servis1.desc = 'Web development refers to building, creating, and an maintaining websites. and database management. A web developer may be involved in designing a website, but may also write web scripts in languages such as PHP and python'
    servis2 = servises()
    servis2.name = 'UI/ux design'
    servis2.desc = 'UX-UI Designers are generally responsible for collecting, researching, investigating and evaluating user requirements. Their responsibility is to deliver an outstanding user experience providing an exceptional and intuitive application design.'
    servis3 = servises()
    servis3.name = 'Web design'
    servis3.desc = 'Web designers plan, create and code internet sites and web pages, many of which combine text with sounds, pictures, graphics and video clips. A web designer is responsible for creating the design and layout of a website or web pages.'
    servis4 = servises()
    servis4.name = 'seo optimize'
    servis4.desc = '    Quality of traffic. You can attract all the visitors in the world, but if they\'re coming to your site because Google tells them you\'re a resource for Apple computers when really you\'re a farmer selling apples, that is not quality traffic. Instead you want to attract visitors.'
    return render(request,'index.html',{'servis1':servis1,'servis2':servis2,'servis3':servis3,'servis4':servis4})