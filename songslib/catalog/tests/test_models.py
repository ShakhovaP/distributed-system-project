from django.test import TestCase

# Create your tests here.

from catalog.models import Singer

class SingerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Singer.objects.create(name='Beyonce_Test', description='Some Test information')

    def test_name_label(self):
        singer =Singer.objects.get(id=1)
        field_label = singer._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_description_label(self):
        singer=Singer.objects.get(id=1)
        field_label = singer._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_name_max_length(self):
        singer=Singer.objects.get(id=1)
        max_length = singer._meta.get_field('name').max_length
        self.assertEquals(max_length,100)

    def test_string_method(self):
        singer=Singer.objects.get(id=1)
        expected_object_name = '%s' % (singer.name)
        self.assertEquals(expected_object_name,str(singer))

    def test_get_absolute_url(self):
        singer=Singer.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(singer.get_absolute_url(),'/catalog/singers/1')