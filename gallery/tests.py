from django.test import TestCase
from django.test import TestCase
from .models import Editor,Images
import datetime as dt

# Create your tests here.
class ImagesTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.Steve= Editor(first_name = 'Steve', last_name ='Kebaso', email ='ongatikebaso@gamil.com')
        self.Steve.save_editor()

        self.new_image= Images(title = 'Test Images',post = 'This is a random test Post',editor = self.Steve)
        self.new_image.save()

        

    def tearDown(self):
        Editor.objects.all().delete()
        Images.objects.all().delete() 
                
    def test_get_gallery_today(self):
        today_gallery = Images.todays_gallery()
        self.assertTrue(len(today_gallery)>0)  
      
    def test_get_gallery_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)
        self.assertTrue(len(gallery_by_date) == 0)        