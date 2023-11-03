# from django.http import HttpResponse
from django.shortcuts import render
from primary_app.models import Album, Musician
from primary_app import forms

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title': 'Home Page', 'musician_list': musician_list}
    return render(request,'primary_app/index.html', context= diction)


def album_list (request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_info = Album.objects.filter(artist=artist_id).order_by('name')
    # pk primary key called by get
    diction = {'title': 'List of Albums', 'artist_info': artist_info, 'albumInfo': album_info}
    return render(request,'primary_app/album_list.html', context= diction)


def musician_form(request):
    form = forms.MusicianForm()
    
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    diction ={'title': 'Add Musician', 'musician_form': form}
    return render(request,'primary_app/musician_form.html', context=diction)

def album_form(request):
    form = forms.AlbumForm()
    
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
    diction = {'title': 'Add Album', 'album_form': form}
    return render(request,'primary_app/album_form.html', context=diction)


def edit_artist(request, artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=artist_info)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = forms.MusicianForm()
    diction = {'edit_form': form}
    return render(request,'primary_app/edit_artist.html', context=diction)

def edit_album(request, album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction = {}
    if(request.method == 'POST'):
        form = forms.AlbumForm(request.POST,instance=album_info)
        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'Successfully Updated!'})
    else:
        form = forms.AlbumForm()
    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request,'primary_app/edit_album.html', context=diction)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction ={'delete_success':'Deleted Successfully'}
    return render(request, 'primary_app/deleted.html', context=diction)\
        

def delete_Musician(request, artist_id):
    artist = Musician.objects.get(pk=artist_id).delete()
    diction ={'delete_success':'Musician Deleted Successfully'}
    return render(request, 'primary_app/deleted.html', context=diction)


