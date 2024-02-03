from django.shortcuts import render

from . import models
import json

# Create your views here.
def index(request):
    data = {'data':models.movies.objects.all().values()}
    #print(models.mpaaRating.objects.all().values())
    #readDataInsertData(request)
    return render(request,"movies/index.html",data)

def detail(request):
    if request.method == 'POST':
        id = request.POST['movie']
    movie = models.movies.objects.filter(id=id).values()[0]
    mpaaRating = models.mpaaRating.objects.filter(id=id).values()[0]
    data = {'movie':movie , 'mpaaRating': mpaaRating}
    #print(data)
    return render(request,"movies/detail.html",data)


def readDataInsertData(request):
    file_name = "movies.json"
    file = open(file_name)
    data = json.loads(file.read())
    for movie in data:
        mpaaRating = movie['mpaaRating']
        mpaaRating = {**{'id_id' : movie['id']},**mpaaRating}
        del movie['mpaaRating']
        movie['genre'] = ', '.join(movie['genre'])
        #print(movie)
        #print(mpaaRating)
        
        models.movies(**movie).save()
        models.mpaaRating(**mpaaRating).save()
    print("all data inserted")