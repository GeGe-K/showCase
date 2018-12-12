from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Photo,Category


# Create your views here.
def index(request):
    # Function that renders the index page
    pics = Photo.get_all_photos()
    return render(request, 'index.html', {"pics":pics})

def photo(request, photo_id):
    try:
        photo = Photo.objects.get(id=photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"search.html", {"photo":photo})

def search_photo(request):
    # Function to implement search
    if 'photo' in request.GET and request.GET["photo"]:
        category = request.GET.get("photo")
        searched_photos = Photo.search_photo(category)
        message = f'{category}'

        return render(request, 'search.html',{"message":message,"photos":searched_photos})
    else:
        message = "You haven't searched for any category"
        return render (request,'search.html',{"message":message})

def filter_by_category(request,category_id):
    
    # Function to filter the db and search for the photo according the category

    photos = Photo.filter_by_category(id = category_id)
    return render(request,'category.html',{"photos":photos})
