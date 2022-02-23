from django.db import models

# Create your models here.
class Partners(models.Model):
    name = models.CharField(max_length=100, )
    logo = models.FileField(upload_to='logos')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    Category =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='projimages', null=True)
    video = models.FileField(upload_to='projvideos', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=True)


    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-id',) 


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    testimony = models.TextField()
    image = models.ImageField(upload_to='images', default="", blank=True, null=True)


    def __str__ (self):
        return self.name    

    class Meta:
        verbose_name_plural= 'Feedbacks'
        ordering = ('-id',)       

class Contact(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300)
    message = models.TextField()

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ('-id',) 

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='projimages', blank=True, null=True) 

    def __str__ (self):
        return self.project.title


    class Meta:
        verbose_name_plural = 'ProjectImages'
        ordering = ('-id',)


