# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User

import datetime
from django.core.validators import RegexValidator





Razas=(
    ("Chihuahua","Chihuahua"),
    ("Poodle","Poodle"),
    ("Labrador","Labrador"),
    ("Pitbull","Pitbull"),
    ("Pastor Aleman","Pastor Aleman"),
    ("Husky","Husky"),
    ("Otro","Otro"),
)


EstadoA=(
    ("Adoptado","Adoptado"),
    ("Encontrado","Encontrado"),
    ("Se Busca","Se Busca"),
    ("Encontrado","Encontrado"),
)





class Posts(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Nombre = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    #Nombre = models.CharField(max_length=120)
    Edad = models.IntegerField()
    Raza = models.CharField(max_length=48, choices=Razas)
    Estado = models.CharField(max_length=48, choices=EstadoA)
    Informacion= models.TextField()
    Descripcion= models.TextField()
    Foto = models.ImageField(null=True, blank=True)
    Autor= models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)



    update = models.DateTimeField(auto_now=True,auto_now_add=False)
    marcadetiempo = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.Nombre

    def get_absolut_url(self):
        return reverse("detalle", kwargs={"abc": self.id})

    @property
    def get_content_type(self):
        instance=self
        content_type=ContentType.objects.get_for_model(instance.__class__)
        return content_type


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):

        content_type=ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs



class Comment(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)


    content_type=models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')




    #post=models.ForeignKey(Posts)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    objects = CommentManager()

    def __unicode__(self):
        return self.content




class usuarios(models.Model):
    name=models.OneToOneField(User)
    Edad=models.IntegerField()
    Telefono=models.IntegerField()
    Email=models.CharField(max_length=48, default="correo@servicio.com")
    Direccion=models.TextField()
    Descripcion=models.TextField()
    Foto = models.ImageField(null=True, blank=True)

    #Imagen = models.ImageField(upload_to='img', blank=True, null=True)

    def __unicode__(self):
        return self.name.email
# Create your models here.
