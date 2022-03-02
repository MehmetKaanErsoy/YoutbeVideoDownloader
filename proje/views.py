from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from pytube import YouTube
import os
from django.contrib import messages


# Create your views here.


def home(request):
    return render(request, 'index.html')


def download(request):
    a = 100
    global search
    search = request.GET.get('search')
    video = YouTube(search)
    title = video.title
    cozunurlukler_list = []
    cozunurlukler = video.streams.filter(progressive=True).all()
    for i in cozunurlukler:
        cozunurlukler_list.append(i.resolution)

    cozunurluk_list = list(dict.fromkeys(cozunurlukler_list))
    return render(request, 'download.html',
                  {'list': cozunurluk_list, 'search': search, 'cozunurlukler': cozunurlukler
                      , 'title': title})


def indirme_bitti(request, resolution):
    global search
    homedir = os.path.expanduser("~")
    uzantı = homedir + '/Downloads'
    YouTube(search).streams.get_by_resolution(resolution).download(uzantı)
    return redirect('home')
