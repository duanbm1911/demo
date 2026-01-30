from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Event, Gallery, About, Contact

def home(request):
    featured_events = Event.objects.filter(is_active=True, is_featured=True)[:3]
    context = {
        'featured_events': featured_events,
    }
    return render(request, 'core/home.html', context)

def about(request):
    about_content = About.objects.filter(is_active=True)
    context = {
        'about_content': about_content,
    }
    return render(request, 'core/about.html', context)

def events(request):
    all_events = Event.objects.filter(is_active=True)
    context = {
        'events': all_events,
    }
    return render(request, 'core/events.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, is_active=True)
    context = {
        'event': event,
    }
    return render(request, 'core/event_detail.html', context)

def gallery(request):
    gallery_items = Gallery.objects.filter(is_active=True)
    context = {
        'gallery_items': gallery_items,
    }
    return render(request, 'core/gallery.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, 'Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi trong thời gian sớm nhất.')
        return redirect('contact')
    
    return render(request, 'core/contact.html')

def robots_txt(request):
    return render(request, 'robots.txt', content_type='text/plain')
