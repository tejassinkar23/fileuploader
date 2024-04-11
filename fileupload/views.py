from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth import authenticate, login
# from .views import home
# Create your views here.
from .models import FilesUpload
def upload(request):
    if request.method == 'POST':
        file2 = request.FILES['file']
        document = FilesUpload.objects.create(file=file2)
        document.save()
        return HttpResponse('File uploaded successfully')
    return render(request, 'fileupload.html')
def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('upload')  # Change 'home' to the name of your homepage URL pattern.
        else:
            # Return an 'invalid login' error message.
            return render(request, 'index.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'index.html')