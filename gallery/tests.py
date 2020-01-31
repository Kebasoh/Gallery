from django.test import TestCase
from django.test import TestCase
from .models import Editor,Images

# Create your tests here.
class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.Steve= Editor(first_name = 'Steve', last_name ='Kebaso', email ='ongatikebaso.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.Steve,Editor))   
    # Testing Save Method
    def test_save_method(self):
        self.Steve.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)          