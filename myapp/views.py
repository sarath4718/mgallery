from django.shortcuts import render, redirect

from myapp.forms import MovieForm

from django.contrib import messages

from django.views.generic import View

from myapp.models import Movies

# Create your views here.

class MovieCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(**data)

            messages.success(request,"movie has been successfully added")

            return redirect("movie-list")
        else:

            messages.error(request,"failed to add movie")
            
            return render(request,"movie_add.html",{"form":form_instance})

class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})

class MovieDetailView(View):
    
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        
        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{"movie":qs})

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id= kwargs.get("pk")

        Movies.objects.get(id=id).delete()

        messages.

        return redirect("movie-list")
    
class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie=Movies.objects.get(id=id)

        movie_dict={
            "title":movie.title,
            "genre":movie.genre,
            "language":movie.language,
            "year":movie.year,
            "run_time":movie.run_time,
            "director":movie.director
        }



        form_instance=MovieForm(movie_dict)

        return render(request,"movie_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get("pk")

            Movies.objects.filter(id=id).update(**data)

            return redirect("movie-list")
        else:

            return render(request,"movie_edit.html",{"form":form_instance})

