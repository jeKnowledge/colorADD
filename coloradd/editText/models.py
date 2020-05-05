from django.db import models
from django import forms


class Post(models.Model):
    contract = models.CharField(max_length=20,choices=[('Type',"Type of Contract"),('company',"Company/Enterprise"),('Municipality',"Municipality"),('School',"School/College"),('Hospital',"Hospital"),('Individual',"Individual"),('Other',"Other")])
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20,choices=[('Subject',"Subject matter"),('Licensing',"Licensing"),('Employment',"Employment"),('ColorADD Social',"ColorADD Social"),('Founds/Donations',"Founds/Donations"),('Other subject',"Other subject")])
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.name + str(self.email)

class Clothing(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="clothing/");

class Environment(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="environment/");

class Game(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="game/");

class Health(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="health/");

class Transport(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="transport/");

class Supplies(models.Model):
    picture = models.ImageField(null=True, blank=True, upload_to="supplies/");

class Noticias(models.Model):
    texto = models.TextField();
    titulo = models.TextField();
    imagem = models.ImageField(null=True, blank=True, upload_to="pictures/");
# Create your models here.
