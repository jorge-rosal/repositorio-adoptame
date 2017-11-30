# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Posts , User, usuarios, Comment, CommentManager
from .forms import PostForm, users_form,CommentForm
from django.views.generic  import FormView
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
# Create your views here.

def inicio(request):
    return render(request, 'app/inicio.html')

def index(request):
    #queryset_list= Posts.objects.active()
    queryset= Posts.objects.all()
    query = request.GET.get("q")
    if query:
        queryset=Posts.objects.filter(
            Q(Raza=query) |
            Q(Informacion=query) |
            Q(Nombre=query) |
            Q(Estado=query)


            ).distinct()

    else:
        queryset= Posts.objects.all()

    context = {
        "object_list": queryset,
        "titulo": "List"

    }
    queryset_list = Posts.objects.all().order_by('-marcadetiempo')
    paginator = Paginator(queryset_list, 3)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
		# If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
    context = {
		"object_list": queryset
	}
    return render(request, 'app/home.html',context)


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'app/perfil.html', {"user":user})

def perfil_view(request):
    queryset= usuarios.objects.all()
    obj=Posts.objects.filter(Autor=request.user)
    context = {
        "object_list": queryset,
        "object_list": obj,
        "titulo": "List"

    }
    return render(request, 'app/perfil.html',context)

def vista1_view(request):
    query = request.GET.get("q")
    obj=Posts.objects.filter(Raza=query)
    return render (request,'app/vista1.html', {"object_list":obj})

def post_create(request):
    if request.user.is_authenticated():
            form = PostForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                user1=request.user

                instance= form.save(commit=False)
                instance.Autor= user1
                instance.save()

                messages.success(request, "Listo")
                return HttpResponseRedirect(instance.get_absolut_url())
                context={
                "form":form


                }
            else:

                context={"form":form} #me falta poner como se veria 404 en produccion por ahora sale error nadamas




    return render(request, 'app/post_create.html', context)

def post_detail(request, abc=None):
    #instance = Post.objects.get(id=1)
    instance= get_object_or_404(Posts, id=abc)
    #content_type = ContentType.objects.get_for_model(Posts)
    #obj_id = instance.id
    initial_data={
        "content_type" : instance.get_content_type,
        "object_id": instance.id


    }


    form=CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type=form.cleaned_data.get("content_type")
        content_type=ContentType.objects.get(model=c_type)
        obj_id=form.cleaned_data.get('object_id')
        content_data=form.cleaned_data.get("content")

        new_comment, created = Comment.objects.get_or_create(
                                    user = request.user,
                                    content_type = content_type,
                                    object_id=obj_id,
                                    content= content_data

                                    )

    #comments = Comment

    comments= Comment.objects.filter_by_instance(instance).order_by('-timestamp')
    #comments = Comment()
    context = {
        #"titulo": instance.Nombre,
        "instance": instance,
        "comments": comments,
        "comment_form":form,
    }

#    if request.user.is_authenticated():
#            context = {
#                "titulo": "Logeado"
#            }
#    else:
#            context = {
#                "titulo": "No logeado"
#            }

    return render(request, 'app/post_detail.html',context)

def post_update(request, abc=None):
    instance= get_object_or_404(Posts, id=abc)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
        messages.success(request, "Se actualizo")

        return HttpResponseRedirect(instance.get_absolut_url())

    context = {
        "titulo": instance.Nombre,
        "instance": instance,
        "form":form,

    }
    return render(request, 'app/post_create.html',context)


def post_delete(request):
    return render(request, 'app/vista1.html')



class registrate(FormView):
    template_name= 'app/registrate.html'
    form_class=users_form
    success_url = reverse_lazy('login')


    def form_valid(self, form):
            p=usuarios()
            user=form.save()
            p.name=user
            p.Telefono=form.cleaned_data['Telefono']
            p.Email=form.cleaned_data['Email']
            p.Edad=form.cleaned_data['Edad']
            p.Foto=form.cleaned_data['Foto']
            p.Direccion=form.cleaned_data['Direccion']
            p.Descripcion=form.cleaned_data['Descripcion']



            p.save()
            return super(registrate, self).form_valid(form)


def raza_Chihuahua(request):
    obj=Posts.objects.filter(Raza="Chihuahua")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Poodle(request):
    obj=Posts.objects.filter(Raza="Poodle")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Labrador(request):
    obj=Posts.objects.filter(Raza="Labrador")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Pitbull(request):
    obj=Posts.objects.filter(Raza="Pitbull")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Pastor(request):
    obj=Posts.objects.filter(Raza="Pastor Aleman")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Husky(request):
    obj=Posts.objects.filter(Raza="Husky")
    return render (request,'app/home.html', {"object_list":obj})

def raza_Otro(request):
    obj=Posts.objects.filter(Raza="Otro")
    return render (request,'app/home.html', {"object_list":obj})


def misPost(request):
    obj=Posts.objects.filter(Raza="Husky")
    return render (request,'app/home.html', {"object_list":obj})
