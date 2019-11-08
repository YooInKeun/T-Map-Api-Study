from django.shortcuts import render, get_object_or_404, redirect
import json

def home(request):
    return render(request, 'index.html')

def post(request):
    if request.method == 'POST':
        lonlat=json.loads(request.body)
        print('경도: ' + str(lonlat['lon'])) # 세로선
        print('위도: ' + str(lonlat['lat'])) # 가로선
    return redirect('home')