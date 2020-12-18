from django.db.models import *
from django.utils.translation import gettext_lazy as _


# Create your models here.
class InstantContent(Model):
    """
    The content that can be easily previewed and transmitted：

        contentType: IntegerField
            1: 'text & image'([pure text] OR [pure image] OR [text + image])
            2: 'location'
            3: 'voice'

        content: BinaryField
            binary version of the content, it should contain all the information of the InstantContent

        compressionMethod: CharField
            1: 'gzip'

        textVersionContent: TextField
            text version of the content, the value should be:
                if the type is pure text:
                    the original pure text
                if the type is pure image:
                    blank
                if the type is text + image:
                    only the text content
                if the type is location:
                    GPS: (xxx.xxx,yyy.yyy,zzz.zzz)
                    Location: provided by the user or Google API
                if the type is voice:
                    the converted text content
    """
    class ContentType(IntegerChoices):
        TYPE_TEXT_IMAGE = 1, _("Text & Image")
        TYPE_LOCATION = 2, _("Location")
        TYPE_VOICE = 3, _("Voice")

    contentType = IntegerField(choices=ContentType.choices)

    def _str_(self):
        return self.title


class InstantContentDraft(InstantContent):
    """
        same as above, but not finished yet, no textVersionContent needed
    """
    pass


class File(Model):
    """
        uploadAs: FileField
            the file should be uploaded to "files/$uid/finished/$fileName"
    """


class UploadingFile(Model):
    """
        uploadAs: FileField
            the file should be uploaded as "files/$uid/$filePathAbove/$count"
        completeFileHash: CharField
    """
