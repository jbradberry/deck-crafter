from io import BytesIO

from django.core.files.images import ImageFile
from django.test import TestCase
from django.urls import reverse

from PIL import Image

from .. import models


class GameListViewTest(TestCase):
    def test_empty(self):
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)

    def test_game_with_no_image(self):
        game = models.Game.objects.create(name="Magic", description="The CCG everyone plays.")
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Magic")
        self.assertContains(response, "The CCG everyone plays.")

    def test_game_with_image(self):
        file_obj = BytesIO()
        image = Image.new('RGB', (100, 50))
        image.save(file_obj, 'png')
        file_obj.seek(0)

        game = models.Game.objects.create(name="Magic", description="The CCG everyone plays.",
                                          image=ImageFile(file_obj, name='logo.png'))
        response = self.client.get(reverse('game_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Magic")
        self.assertContains(response, "The CCG everyone plays.")
        self.assertContains(response, 'width="80" height="40"')
