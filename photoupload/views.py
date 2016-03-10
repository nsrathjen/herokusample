from django.shortcuts import render_to_response
from django.template import RequestContext
from photoupload.models import Picture
from photoupload.forms import PictureForm

# Create your views here.
def list_pictures(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        newpic = Picture(picfile = request.FILES['picfile'])
        newpic.save()

    else:
        form = PictureForm()

    pictures = Picture.objects.all()

    return render_to_response('photoupload/main.html', {'pictures': pictures, 'form': form}, context_instance = RequestContext(request))
