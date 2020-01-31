from django.test import TestCase
from django.test import TestCase
from django.test import TestCase
from .models import Editor,Images,tags
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.Steve= Editor(first_name = 'Steve', last_name ='Kebaso', email ='ongatikebaso@gmail.com')
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Steve,Editor))  
        
   # Testing Save Method
    def test_save_method(self):
        self.Steve.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)       

class imagesTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.Steve= Editor(first_name = 'Steve', last_name ='Kebaso', email ='ongatikebaso@gamil.com')
        self.Steve.save_editor()

        self.new_image= images(title = 'Test images',post = 'This is a random test Post',editor = self.Steve)
        self.new_image.save()

        

    def tearDown(self):
        Editor.objects.all().delete()
        images.objects.all().delete() 
                
    def test_get_gallery_today(self):
        today_gallery = images.todays_gallery()
        self.assertTrue(len(today_gallery)>0)  
      
    def test_get_gallery_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)
        self.assertTrue(len(gallery_by_date) == 0)        