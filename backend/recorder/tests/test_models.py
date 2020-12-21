from django.test import TestCase

from recorder.models.site_application import InstantContent
from recorder.models.core import *


class SingleModelTestCase(TestCase):
    def setUp(self):
        InstantContent.objects.create(contentType=InstantContent.ContentType.TYPE_LOCATION)

    def test_user_instant_content(self):
        some_one_voice_content: InstantContent = InstantContent.objects.get(
            contentType=InstantContent.ContentType.TYPE_LOCATION)
        user = some_one_voice_content.user
        all_users = RecordedUser.objects.all()
        self.assertEqual(all_users.count(),0)

        self.assertEqual(1, 1)
