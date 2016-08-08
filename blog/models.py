from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Beliefs(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def publish(self):
        self.published_date = datetime.auto_now()
        self.save()

    def __str__(self):
        return self.title
    """
    def save(self, *args, **kwargs):
        # do_something()
        super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
        # do_something_else()
    """






class Org(models.Model):
    name = models.CharField(max_length=200) # Should link to its site
    info = models.TextField()

    def __str__(self):
        return self.name

    def all_data(self): # Use for search algorithms, maybe this isn't the best...
        return self.name + self.info


class Search(models.Model):
    search_input = models.CharField(max_length=200)

    def __str__(self):
        return self.search_input





class Vari(models.Model):
    value = models.CharField(max_length=100)
    type1 = models.CharField(default="one", max_length=100)

    def __str__(self):
        return (self.value, self.type)


class NewsFeed(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/media/uploads/', blank=True, null=True )
    """
    CHANNGE THE ABOVE!! WHY DID THIS FIX IT?
    """
    # storage=FileSystemStorage(location=settings.MEDIA_ROOT) maybe add to imagefield variables
    published_date = models.DateTimeField(default=datetime.now(), blank=True)



    def __str__(self):
        return self.title
