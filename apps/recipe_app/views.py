from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt
import requests

def getRecipeById(id):

    headers={
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
  }
    endpoint = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    r = requests.get(endpoint, headers = headers)
    results = r.json()
    return results

def searchRecipes(query):
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
        }
    params = { 
        'query' :query,
        'number' : 15
     }
    r = requests.get(endpoint,params = params, headers = headers)
    results = r.json()
    return results

def randomrecipe():
    endpoint="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
    }
    r = requests.get(endpoint,headers = headers)
    results = r.json()
    return results

def filterbyCuisine(cuisine):
    endpoint="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
    }
    params = {
        'cuisine' : cuisine,
        'number'  : 15
    }
    r = requests.get(endpoint,params = params, headers = headers)
    results = r.json()
    return results

def jokes():
    endpoint="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/jokes/random"
    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
    }
    r = requests.get(endpoint, headers=headers)
    jokes = r.json()
    return jokes
# Create your views here.
def index(request):
    return render(request, 'index.html')


def browse(request):
    return render(request, 'browse.html')
def test(request):
    context = {
        'recipes' : filterbyCuisine('cambodian')["results"]
    }
    return render(request, 'test.html',context)

def showrecipe(request,id):
    context = {
        'recipe' : getRecipeById(int(id))
    }
    return render(request,'detail.html',context)

def search(request):
    search = request.POST["search"]
    context = {
        'recipes' : searchRecipes(search)["results"]
    }
    return render(request, 'browse.html',context)

def surprise(request):
    context = {
        'recipe' :randomrecipe()["recipes"][0]
    }
    return render(request,'detail.html',context)

def home(request):
    if not "id" in request.session:
        return redirect('/')
    else:
        print(request.session["id"])
        context={
            'user': User.objects.get(id=request.session["id"]),
            'joke' : jokes()["text"],
            'featured1' : randomrecipe()["recipes"][0],
            'featured2' : randomrecipe()["recipes"][0],
            'featured3' : randomrecipe()["recipes"][0],
            'featured4' : randomrecipe()["recipes"][0]
        }
        return render(request, 'home.html',context)


def register(request):
    print("Errors include:")       
    errors = User.objects.register_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.warning(request,value)
        return redirect('/')
    else:
        hashedpw = bcrypt.hashpw(request.POST["pw"].encode(),bcrypt.gensalt())
        print(hashedpw)
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email = request.POST["email"],password = hashedpw)
        request.session["id"]= User.objects.last().id
        return redirect('/welcome')


def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        request.session["id"] = User.objects.get(email = request.POST["email"]).id
    return redirect('/welcome')

def logout(request):
    del request.session["id"]
    return redirect('/')