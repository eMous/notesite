from django.db.models import Model, IntegerChoices, CASCADE, ForeignKey, IntegerField, BinaryField, TextField, \
    FileField, URLField

from .core import RecordedUser
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

    class CompressionMethod(IntegerChoices):
        TYPE_GZIP = 1, _("gzip")

    user = ForeignKey(to=RecordedUser, on_delete=CASCADE,null=True)
    contentType = IntegerField(choices=ContentType.choices,null=True)
    content = BinaryField(null=True)
    compressionMethod = IntegerField(choices=CompressionMethod.choices, null=True)
    textVersionContent = TextField(null=True)

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
        downloadUrl: UrlField
            the url to directly download the file
    """
    uploadAs = FileField(null=True)
    downloadUrl = URLField(null=True)


class UploadingFile(Model):
    """
        uploadingDir: FileField
            the file should be uploaded as "files/$uid/$filePathAbove/$count"
    """
    uploadingDir = FileField(null=True)
