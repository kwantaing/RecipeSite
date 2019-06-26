from django.shortcuts import render, HttpResponse
import requests

def getRecipeById(id):

    headers={
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
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
        "X-RapidAPI-Key": "70cfe9b480msh6003ae8a99fd83fp1a0e1djsn2384d115aca9"
        }
    params = { 
        'query' :query,
        'number' : 15
     }
    r = requests.get(endpoint,params = params, headers = headers)
    results = r.json()
    print(results)
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
    print(results)
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

def home(request):
    context = {
        'joke' : jokes()["text"]
    }
    return render(request, 'home.html',context)

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