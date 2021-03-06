from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Image, Location, Category
from cloudinary.forms import cl_init_js_callbacks      
from .models import Image
from .forms import ImageForm
from django.contrib import messages 



# Create your views here.
def main(request):
    try:        
        images = Image.objects.all()
        category = Category.objects.all()
        location = Location.objects.all()
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'index.html', {'images':images, 'category':category, 'location':location})

def search_images(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_category)

        return render(request, 'search.html',{"message":message,"image": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})

def view_by_location(request,location):
    try:
        image_location = Image.filter_by_location(location)
        message = location
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'location.html',{"location": image_location, 'message':location})

def add_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return False
    
    return render(request, 'form.html', {'form':ImageForm,})
    
