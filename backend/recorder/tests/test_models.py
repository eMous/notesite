from django.test import TestCase

from recorder.models.site_application import InstantContent


class SingleModelTestCase(TestCase):
    def setUp(self):
        InstantContent.objects.create(contentType=InstantContent.ContentType.TYPE_VOICE)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""

        someOneVoiceContent = InstantContent.objects.get(contentType=InstantContent.ContentType.TYPE_VOICE)
        self.assertEqual(someOneVoiceContent.contentType, InstantContent.ContentType.TYPE_LOCATION)