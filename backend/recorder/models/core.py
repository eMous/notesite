from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from .model_conf import ModelConf


class RecordedUser(User):
    class Meta:
        proxy = True



class Record(models.Model):
    """
        time: DatetimeField
        timeZone: CharField
        gpsLat: DecimalField
        gpsLon: DecimalField
        deviceName: CharField
        deviceType: CharField
            1: PC
            2: Mac
            3: Android Phone
            4: iPhone
            5: iPad
        browserName: CharField
        softwareName: CharField
        softwareVersion: CharField
        other: textField
        operationType: CharField
            1. Add
            2. Modify
            3. Delete
            4. Login
            5. Logout
            6. Leave
    """

    class DeviceType(models.IntegerChoices):
        TYPE_PC = 1, _("PC")
        TYPE_MAC = 2, _("Mac")
        TYPE_ANDROID_PHONE = 3, _("Android Phone")
        TYPE_IPHONE = 4, _("iPhone")
        TYPE_IPAD = 5, _("iPad")

    class OperationType(models.IntegerChoices):
        TYPE_ADD = 1, _("Add")
        TYPE_MODIFY = 2, _("Modify")
        TYPE_DELETE = 3, _("Delete")
        TYPE_LOGIN = 4, _("Login")
        TYPE_LEAVE = 5, _("Logout")
        TYPE_LOGOUT = 6, _("Leave")

    time = models.DateTimeField(null=True)
    timeZone = models.CharField(max_length=ModelConf.lowCharLenMax, null=True)
    gpsLat = models.DecimalField(decimal_places=ModelConf.highDecimalPlace, max_digits=ModelConf.gpsMaxDigit, null=True)
    gpsLon = models.DecimalField(decimal_places=ModelConf.highDecimalPlace, max_digits=ModelConf.gpsMaxDigit, null=True)
    deviceName = models.CharField(max_length=ModelConf.lowCharLenMax, null=True)
    deviceType = models.IntegerField(choices=DeviceType.choices, null=True)
    browserName = models.CharField(max_length=ModelConf.middleCharLenMax, null=True)
    softwareName = models.CharField(max_length=ModelConf.lowCharLenMax, null=True)
    softwareVersion = models.CharField(max_length=ModelConf.lowCharLenMax, null=True)
    other = models.TextField(null=True)

