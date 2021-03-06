from datetime import date
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class UserProject(models.Model): #should be called members
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #this is actually the owner
    members = models.ManyToManyField(User, related_name='group_member', blank=True, through=UserProject) #to store list of people
    title = models.TextField(blank=False, null=False)
    begin_date = models.DateField(default=date.today, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    progress = models.BooleanField(default=True, null=False)

    class Meta:
        ordering = ['-id']

    #for if i need to include this
    #@property
    #def do_something(self):
    #    return 2
    