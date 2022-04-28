from django.test import TestCase

# Create your tests here.

from catalog.models import Song
from catalog.models import Singer

from django.urls import reverse

class SongsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 23 songss for pagination tests
        number_of_songs = 23
        for song_num in range(number_of_songs):
            Song.objects.create(name='Some song %s' % song_num, singer =  Singer.objects.create(name='Singer_Test %s' % song_num, description='Some Test information %s' % song_num))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/songs/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('songs'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('songs'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalog/song_list.html')

    def test_pagination_is_twenty(self):
        resp = self.client.get(reverse('songs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['song_list']) == 20)

    def test_lists_all_songs(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('songs')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['song_list']) == 3)