# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Año(models.Model):

    #__Año_FIELDS__
    anio = models.CharField(max_length=255, null=True, blank=True)

    #__Año_FIELDS__END

    class Meta:
        verbose_name        = _("Año")
        verbose_name_plural = _("Año")


class Categoria(models.Model):

    #__Categoria_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Categoria_FIELDS__END

    class Meta:
        verbose_name        = _("Categoria")
        verbose_name_plural = _("Categoria")


class Grado(models.Model):

    #__Grado_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Grado_FIELDS__END

    class Meta:
        verbose_name        = _("Grado")
        verbose_name_plural = _("Grado")


class Alta(models.Model):

    #__Alta_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Alta_FIELDS__END

    class Meta:
        verbose_name        = _("Alta")
        verbose_name_plural = _("Alta")


class Tramite(models.Model):

    #__Tramite_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Tramite_FIELDS__END

    class Meta:
        verbose_name        = _("Tramite")
        verbose_name_plural = _("Tramite")


class Unidad(models.Model):

    #__Unidad_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Unidad_FIELDS__END

    class Meta:
        verbose_name        = _("Unidad")
        verbose_name_plural = _("Unidad")


class Especialidad(models.Model):

    #__Especialidad_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    alta = models.ForeignKey(Alta, on_delete=models.CASCADE)

    #__Especialidad_FIELDS__END

    class Meta:
        verbose_name        = _("Especialidad")
        verbose_name_plural = _("Especialidad")


class Concurso(models.Model):

    #__Concurso_FIELDS__
    anio = models.ForeignKey(Año, on_delete=models.CASCADE)

    #__Concurso_FIELDS__END

    class Meta:
        verbose_name        = _("Concurso")
        verbose_name_plural = _("Concurso")


class Especialidadunidad(models.Model):

    #__Especialidadunidad_FIELDS__
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    concurso = models.ForeignKey(Concurso, on_delete=models.CASCADE)
    vacantes = models.IntegerField(null=True, blank=True)
    activo = models.BooleanField()

    #__Especialidadunidad_FIELDS__END

    class Meta:
        verbose_name        = _("Especialidadunidad")
        verbose_name_plural = _("Especialidadunidad")



#__MODELS__END
