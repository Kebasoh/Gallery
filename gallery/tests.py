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
              
class ImagesTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.Steve= Editor(first_name = 'Steve', last_name ='Kebaso', email ='ongatikebaso@gmail.com')
        self.Steve.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_images= Images(title = 'Test Images',post = 'This is a random test Post',editor = self.Steve)
        self.new_images.save()

        self.new_images.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()       