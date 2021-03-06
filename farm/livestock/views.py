from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Animal

# Create your views here.

# # Dummy data - will be removed
# cow_list = [
#     {"name": "Daisy", "age": 3, "id": 1},
#     {"name": "Cow", "age": 1, "id": 2},
#     {"name": "Lucy", "age": 7, "id": 3}
# ]

def index(request):
#index view thar returns html
    return HttpResponse("""
    <h1>Livestock</h1>
    <i>Where animals are things🐮</i>
    """)

def about(request):
    return HttpResponse("""
    <h1>About</h1>
    <p>Sunset Oaks Farm is a happy community of independently-minded cows.</p>
    """)

def cows(request):
    #define data here with a key of cows and a value of a
    data = {
        "cows": Animal.objects.filter(species=3)
    }
    return render(request, 'cows.html', data) #render takes 3 args, request + name of html folder, data
    # return HttpResponse(f"""
    # <h1>Cow list</h1>
    # <p>Currently, we have {len(cow_list)} cows.</p>
    # """)

def cow(request, id):
    #filter takes in func and thing to filter
    data={"cow": get_object_or_404(Animal, pk=id)} #finding primary key matching id
    # data = {"cow": list(filter(lambda c: c["id"] == id, cow_list))[0]}
    return render(request, 'cow.html', data)

def all(request):
    return HttpResponse("""
    <h1>All Animals</h1>
    <p>Here is a list of all our animals for eating:</p>
    <ul>
    <li> 
    Alligator
    </li>
    <li> 
    Ostrich
    </li>
     <li> 
    Kangaroo
    </li>
     <li> 
    Pandas
    </li>
    </ul>
    """)

def shop(request):
    return HttpResponse("""
    <h1>Shop</h1>
    <p>Buy our delicious steaks</p>
    """)

def list_animals(request):
    data = {
        "animals": [animal.to_dict() for animal in Animal.objects.all()]
    }
    return JsonResponse(data)

def list_cows(request):
    data = {
        # "cows": list(Animal.to_dict(c) for c in Animal.objects.filter(species=3)),
        #for each animal in list of animals from db
        # convert it to a dictionary
        #put the dictionary into a list
        "cows": [animal.to_dict() for animal in Animal.objects.filter(species=3)]
    }
    return JsonResponse(data)

def get_cow(request, id):
    data = {
        "cow": get_object_or_404(Animal.objects.filter(species=3), pk=id).to_dict()
    }
    return JsonResponse(data)

def list_alligators(request):
    data = {
        "alligators": [animal.to_dict() for animal in Animal.objects.filter(species=2)]
    }
    return JsonResponse(data)

def get_alligator(request, id):
    data = {
        "alligator": get_object_or_404(Animal.objects.filter(species=2), pk=id).to_dict()
    }
    return JsonResponse(data)

def not_found_404(request, exception):
    return render(request, '404.html')
