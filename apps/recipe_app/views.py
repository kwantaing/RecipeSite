from django.shortcuts import render, HttpResponse
import requests

def getRecipeById(id):

    headers={
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "39e0d510a6msh2032e3c2a8dae62p1d2202jsn13bf3a0ce7dd"
  }
    endpoint = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    r = requests.get(endpoint, headers = headers)
    results = r.json()
    print(results)
    return results

def searchRecipes(query):
    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    headers={
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "39e0d510a6msh2032e3c2a8dae62p1d2202jsn13bf3a0ce7dd"
        }
    params = { 
        'query' :query,
        'number' : 25
     }
    r = requests.get(endpoint,params = params, headers = headers)
    results = r.json()
    print(results)
    return results

def filterbyCuisine(cuisine):
    endpoint="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
    headers = {
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
        "X-RapidAPI-Key": "39e0d510a6msh2032e3c2a8dae62p1d2202jsn13bf3a0ce7dd"
    }
    params = {
        'cuisine' : cuisine,
        'number'  : 25
    }
    r = requests.get(endpoint,params = params, headers = headers)
    results = r.json()
    print(results)
    return results

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def browse(request):
    return render(request, 'browse.html')
def test(request):
    context = {
        'recipes' : filterbyCuisine('japanese')["results"]
    }
    return render(request, 'test.html',context)

def showrecipe(request,id):
    context = {
        'recipe' : getRecipeById(int(id))
    }
    return render(request,'detail.html',context)