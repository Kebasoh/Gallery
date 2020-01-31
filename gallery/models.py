from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    def __str__(self):
        return self.first_name
    
    
    def save_editor(self):
        self.save()
        
    class Meta:
        ordering = ['first_name'] 
        
        
class Images(models.Model):
    title = models.CharField(max_length =30)
    post = models.CharField(max_length =30)
    editor = models.ForeignKey(Editor) 
    pub_date = models.DateTimeField(auto_now_add=True)      
    
    
    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return gallery
    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(pub_date__date = date)
        return gallery