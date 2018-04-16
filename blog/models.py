from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):  #defines our model(as an object)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)

def publish(self):
        self.published_date = timezone.now()
        self.save()
	    
def __str__(self): #methods always return something. This one returns a string(text)
	    return self.title #that is the post title
	

	#note the identation of the methods is inside our class post


		
	


