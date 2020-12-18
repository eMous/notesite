from django.test import TestCase

from recorder.models.site_application import InstantContent, Manufacturer


class SingleModelTestCase(TestCase):
    def setUp(self):
        manu=Manufacturer.objects.create()
        InstantContent.objects.create(contentType=InstantContent.ContentType.TYPE_LOCATION,manufacturer=manu)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""

        someOneVoiceContent:InstantContent = InstantContent.objects.get(contentType=InstantContent.ContentType.TYPE_LOCATION)
        self.assertEqual(someOneVoiceContent.contentType, InstantContent.ContentType.TYPE_LOCATION)

        manu:Manufacturer = Manufacturer.objects.get(kk=12)
        s= manu.instantcontent_set
        d = s.all()
        a=1
