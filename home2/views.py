
# imports that provides the functionality to the view

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.forms.forms import NON_FIELD_ERRORS
from django.urls import reverse

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Availstatic


from .forms import AvailForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .filters import AvailFilter


# View to list all the records alongwith the django-filter

@login_required()
def avail_list(request):
    avails1 = Availstatic.objects.all().order_by('-row_date')
    avail_filter = AvailFilter(request.GET, queryset=avails1)
    avails1 = avail_filter.qs
    
    
    paginator = Paginator(avails1, 144)
    page = request.GET.get('page',1)
    
    try:
        avails = paginator.page(page)
    except PageNotAnInteger:
        avails = paginator.page(1)
    except EmptyPage:
        avails = paginator.page(paginator.num_pages)
    
    context = {
        'paginator': paginator,
        'avails': avails,
        'filter': avail_filter,
    }
    return render(request,'avails/avail_list.html',context)
    
            

# View that renders the django form and saves it to the db

@login_required()
def save_all(request,form,template_name):
    
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            avails = Availstatic.objects.all().order_by('-row_date')
            page = request.GET.get('page', 1)
            paginator = Paginator(avails, 144)
            try:
                avails = paginator.page(page)
            except PageNotAnInteger:
                avails = paginator.page(1)
            except EmptyPage:
                avails = paginator.page(paginator.num_pages)
            data['avail_list'] = render_to_string('avails/avail_list_2.html',{'avails':avails})
        
        else:
            
            data['form_is_valid'] = False
    context = {
    'form':form
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

# View to create a new record in the table

@login_required()
def avail_create(request):
    if request.method == 'POST':
        form = AvailForm(request.POST)
    else:
        form = AvailForm()
    return save_all(request,form,'avails/avail_create.html')


# View to update the table

@login_required()
def avail_update(request,id):
    avail = get_object_or_404(Availstatic,id=id)
    
    if request.method == 'POST':
        form = AvailForm(request.POST,instance=avail)
    else:
        form = AvailForm(instance=avail)
    return save_all(request,form,'avails/avail_update.html')

# View to delete the records

@login_required()
def avail_delete(request,id):
    data = dict()
    avail = get_object_or_404(Availstatic,id=id)

    if request.method == "POST":
        avail.delete()
        data['form_is_valid'] = True
        avails = Availstatic.objects.all().order_by('-row_date')
        page = request.GET.get('page', 1)
        paginator = Paginator(avails, 144)
        try:
            avails = paginator.page(page)
        except PageNotAnInteger:
            avails = paginator.page(1)
        except EmptyPage:
            avails = paginator.page(paginator.num_pages)

        data['avail_list'] = render_to_string('avails/avail_list_2.html',{'avails':avails})
    else:
        context = {'avail':avail}
        data['html_form'] = render_to_string('avails/avail_delete.html',context,request=request)

    return JsonResponse(data)
