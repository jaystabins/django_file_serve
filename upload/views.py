from .models import Image
from .forms import ImageForm
from django.shortcuts import render

# Create your views here.
def index(request):
    images = Image.objects.all()
    context = {
        'images': images
    }
    return render(request, 'upload/index.html', context)

def upload(request):
    context = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get('image')
            obj = Image.objects.create(image=img)
            obj.save()

            context = {
                'images': Image.objects.all()
            }
            return render(request, 'upload/index.html', context)
        print(form.errors)

    context['form'] = ImageForm()
    return render(request, 'upload/upload.html', context)