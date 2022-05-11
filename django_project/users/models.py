from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #that means if the user is deleted profile also will be deleted
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    
    # adding dunder str method so when we print this out how we want to display
    def __str__(self):
      return f'{self.user.username} Profile '
# anytime we make a change in models it changes our databse. so to make these changes 
# affect we need to run migration commands
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
