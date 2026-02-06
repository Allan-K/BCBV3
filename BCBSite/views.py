from urllib import request
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm, TestimonialsForm, EventsForm, LinkForm, GalleryForm, SongsForm
from .models import Songs, Testimonials, Events, Links, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse, Http404, FileResponse
from django.utils import timezone

def index (request):
    flyer = Events.objects.all().order_by('-article_created_at')[:1]
    #time = timezone.now().timestamp()
    print(flyer)
    print(timezone.now())
    return render(request, 'BCB/index.html', {"flyer":flyer})

def confirm(request):
    return render(request, "registration/confirm.html")

def dashboard(request):
    return render(request, "registration/login.html")

def sign_up(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save(commit=False)
            user.is_active = False
            user = form.save()
            
            login(request, user)
            return redirect(reverse("login"))
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/login.html", {"form": form})

#Code dealing with the Music Library

def music(request):
    if request.user.is_authenticated:
        score = Songs.objects.order_by('title').values()
        page_num = request.GET.get('page', 1)
        paginator = Paginator(score, 5)
    
        try:
            items_page = paginator.page(page_num)
            items_page_items = items_page.object_list
        except PageNotAnInteger:
            items_page = paginator.page(1)
        except EmptyPage:
            items_page = paginator.page(paginator.num_pages)
        #score = Songs.objects.all()
        return render(request, "BCB/music.html", { "items_page": items_page})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def search_music(request):
    if request.method == 'GET':
        value = request.GET['title']

        if value == '':
            messages.success(request, "Please enter a search criteria")
            items_page = Songs.objects.all()
        else:
            items_page = Songs.objects.filter(title__startswith = value)
            print('score2', items_page)
        return render(request, "BCB/music.html", {'items_page':items_page})
    
def add_tune(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SongsForm(request.POST, request.FILES)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('music')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = SongsForm()
        return render(request, 'BCB/add_tune.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')  

def edit_music(request, id):
    if request.user.is_authenticated:
        tune = Songs.objects.get(id=id)
        if request.method == 'POST':
            form = SongsForm(request.POST, instance=tune)
            if form.is_valid():
                form.save()
                return redirect('music') # prepopulate the form with an existing band
        else:
            form = SongsForm(instance=tune)
                
        return render(request, 'BCB/edit_music.html',{'form': form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')   

def delete_tune(request, id):
    if request.user.is_authenticated:
        song = get_object_or_404(Songs, id=id)
        song.delete()
        return redirect('music')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

 #Code dealing with Testimonials

def testimonials(request):
    articles = Testimonials.objects.all()
    ordering = ['article_created_at']
    return render(request, 'BCB/testimonials.html', {'articles':articles})

def add_testimonial_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TestimonialsForm(request.POST, request.FILES)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('testimonials')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = TestimonialsForm()
        return render(request, 'BCB/add_testimonial_item.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    

def edit_testimonial(request, id):
    if request.user.is_authenticated:
        edit_img = Testimonials.objects.get(id=id)
        if request.method == "POST":
            edit_img.heading= request.POST['heading']
            edit_img.content_text = request.POST['content_text']
            edit_img.save()        
            return redirect('testimonials')
        print('here')
        edit_img = Testimonials.objects.get(id=id)
        return render(request, 'edit_testimonial.html', {"edit_img":edit_img})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def delete_testimonial_item(request, id):
    if request.user.is_authenticated:
        img = get_object_or_404(Testimonials, id=id)
        img.delete()
        return redirect('testimonials')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
#Code dealing with Events

def events(request):
    articles = Events.objects.all()
    ordering = ['article_created_at']
    return render(request, 'BCB/events.html', {'articles':articles})

def add_events_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventsForm(request.POST, request.FILES)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('events')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = EventsForm()
        return render(request, 'BCB/add_events_item.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

#Code dealing with Links

def links(request):
    links = Links.objects.all()
    ordering = ['article_created_at']
    return render(request, 'BCB/links.html', {'links':links})

def delete_link(request, id):
    if request.user.is_authenticated:
        link = get_object_or_404(Links, id=id)
        link.delete()
        return redirect('links')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def add_link(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = LinkForm(request.POST)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('links')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = LinkForm()
        return render(request, 'BCB/add_link.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

#Code dealing with Gallery

def gallery(request):
    articles = Gallery.objects.all()
    ordering = ['article_created_at']
    return render(request, 'BCB/gallery.html', {'articles':articles})

def add_gallery_item(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GalleryForm(request.POST, request.FILES)
            print('here')
            if form.is_valid():
                form.save()
                return redirect('gallery')
            else:
                print('Not Here')
        else:
            print('here 2')
            form = GalleryForm()
        return render(request, 'BCB/add_gallery_item.html', {'form':form})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def delete_gallery_item(request, id):
    if request.user.is_authenticated:
        img = get_object_or_404(Gallery, id=id)
        img.delete()
        return redirect('gallery')
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')

def edit_gallery(request, id):
    if request.user.is_authenticated:
        edit_img = Gallery.objects.get(id=id)
        if request.method == "POST":
            edit_img.heading= request.POST['heading']
            edit_img.content_text = request.POST['content_text']
            edit_img.save()        
            return redirect('gallery')
        print('here')
        edit_img = Gallery.objects.get(id=id)
        return render(request, 'BCB/edit_gallery.html', {"edit_img":edit_img})
    else:
        messages.success(request, "Please log to access this page")
        return render(request, 'login.html')
    
def hire_us(request):

    return render(request, 'BCB/hire_us.html', {})

def view_404(request):
    return render(request, 'BCB/404.html', status=404)
