from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Dummy data - will be removed
cow_list = [
    {"name": "Daisy", "age": 3, "id": 1},
    {"name": "Cow", "age": 1, "id": 2},
    {"name": "Lucy", "age": 7, "id": 3}
]

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
        "cows": cow_list
    }
    return render(request, 'cows.html', data) #render takes 3 args, request + name of html folder, data
    # return HttpResponse(f"""
    # <h1>Cow list</h1>
    # <p>Currently, we have {len(cow_list)} cows.</p>
    # """)

def cow(request, id):
    #filter takes in func and thing to filter
    data = {"cow": list(filter(lambda c: c["id"] == id, cow_list))[0]}
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
