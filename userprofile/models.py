from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser  
# process avatars and generate thumbnails with pillow and django-imagekit. src="{{ user.avatar.url }}
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from allauth.account.models import EmailAddress
import shutil

# extend django built-in User
class User(AbstractUser):
    # extend avatar column for users. upload_to must be relative path following media/ directory. Front-end avatar.url refers to media/avatar/...
    avatar = ProcessedImageField(
                                upload_to="avatar", 
                                default="avatar/default.png", 
                                verbose_name="avatar",
                                processors=[ResizeToFill(150, 150)], # image size after processing
                                # format="JPEG", # image format after processing
                                options={"quality": 100} # image quality after processing
                                )

    def email_verified(self):
        if self.is_authenticated:
            result = EmailAddress.objects.filter(email=self.email)
            if len(result):
                return result[0].verified
            else:
                return False

    # Override save() of User class to save uploaded avatars
    def save(self, *args, **kwargs):
        # when a user changes the avatar, the image will be stored as: media/avatar/my-username/my-pic.jpg
        if len(self.avatar.name.split("/")) == 1:
            # remove the whole directory so to remove avatars that won't be used anymore to save storage
            shutil.rmtree("./static/media/avatar/"+self.username)
            self.avatar.name = self.username + "/" + self.avatar.name
        # call save() from parent class, so a"vatar.name" becomes "upload_to/username/filename"
        super(User, self).save()

    class Meta:
        # define table name and its plural form in Admin
        verbose_name = "userinfo" 
        verbose_name_plural = verbose_name
        # define the default order shown in admin
        ordering = ["-id"]
    
    # what to show in admin when refer to this table
    def __str__(self):
        return self.username
