
from django.db import models
from django.contrib.auth.models import AbstractUser

#user
class ModelsUser(AbstractUser):
    bio = models.TextField('user bio', max_length=40)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.username}'

#project
class ProjectModels(models.Model):
    title = models.CharField('Project name', max_length=15)
    description = models.TextField('project description', blank=True, null=True)
    owner = models.ForeignKey(ModelsUser, on_delete=models.CASCADE, related_name='owner')
    member = models.ManyToManyField(ModelsUser, related_name='member') 
    start_date = models.DateField('start_date', auto_now=True)
    end_date = models.DateField('end_date')
    
    def __str__(self):
        return f'{self.title}'
    
#task
class TaskModels(models.Model):
    title = models.TextField('Task name', max_length=15)
    description = models.TextField('Task description', max_length=30)
    deadline_date = models.DateField('end date', auto_now=True)
    project = models.ForeignKey(ProjectModels, on_delete=models.CASCADE, related_name='project')
    assigned_to = models.ForeignKey(ModelsUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
