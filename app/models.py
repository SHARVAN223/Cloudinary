from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.storage import MediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


class Media(models.Model):
    Image = models.ImageField(upload_to='images/',storage=MediaCloudinaryStorage())

    Audio = models.FileField(upload_to='audio/',storage=RawMediaCloudinaryStorage())

    Video = models.FileField(upload_to='video/',storage=VideoMediaCloudinaryStorage(),validators=[validate_video])