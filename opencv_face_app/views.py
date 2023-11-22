from django.shortcuts import render

# Create your views here.

def first_view(request):
    return render(request, 'opencv_face_app/first_view.html', {})