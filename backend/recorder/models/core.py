from django.db import models

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
        browserType: CharField
        softwareName: CharField
        softwareVersion: CharField
        other: textField
        operationType: CharField
            1. Add
            2. Modify
            3. Delete
            4. Login
            5. Leave
    """
    pass