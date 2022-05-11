from django.db.models.signals import post_save #this is the signal that got fired after the objects got saved
from django.contrib.auth.models  import User # this is the sender in this case
from django.dispatch import receiver
from .models import Profile # importing this since we are creating profiles

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) # with that we have this function that we want to run when user is created
        #when the user is save by Post_save signal its send the signal 
        # and the signal is received by above function and it  takes all args that 
        # post_save signal pass to it one of those is 
        # instance and one of those is creted
        # this function run each ttime when the user is created and we need  to make save function that save our profile eac time when the user is created
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
     instance.profile.save() # the one more thing we need to do for working this need to import this signal inside of the user apps.py  ready func 