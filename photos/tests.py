from django.test import TestCase
from .models import Image, Location,Category

# Create your tests here.
class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Travel')
        self.name = Category(name='Travel')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Category))
class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(name='Europe')
        self.name = Location(name='Europe')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.name,Location))

  
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Africa')
        self.location.save()

        self.category = Category(name='Fashion')
        self.category.save()

        self.image_test = Image(id=1, image='image.jpg', description='this is a test image', location=self.location,
                                category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()        