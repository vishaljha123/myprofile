import form as form
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.views.generic.base import View

from .models import Userinfo
from django.views.generic import DetailView, ListView
from .forms import Userinformation
from django.views.generic.edit import FormView

class displayuser(ListView):
    model = Userinfo
    template_name = 'userinfo_list.html'

def applyuser(request):
    if request.method == 'POST':
        form = Userinformation(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('success')
    else:
        form = Userinformation()
    return render(request, 'registration.html', {'form': form})



# class displayuserdet(DetailView):
#     model = Userinfo
#     template_name = 'userinfo_detail.html'


# def displayuserdet(request, primary_key):
#     candidate = get_object_or_404(Userinfo, pk=primary_key)
#     return render(request, 'userinfo_detail.html', context={'candidate': Userinfo.email_add})



class displayuserdet(DetailView):

    model = Userinfo
    slug_field = 'phone'

    template_name = 'userinfo_detail.html'
