
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Otp
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from .models import CustomUser


# create token for email verification
def create_token(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            pass
        
        else:
            Otp.objects.create(user=instance, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5)) #set timer
            instance.is_active=False # deactivate the user
            instance.save()
        
        
        # email credentials
        otp = Otp.objects.filter(user=instance).last()
       
       
        subject="Email Verification"
        message = f"""
                                Hi {instance.username}, here is your OTP {otp.otp_code} 
                                it expires in 5 minute, use the url below to redirect back to the website
                                http://127.0.0.1:8000/verify-email/{instance.username}
                                
                                """
        sender = "mycolor.mine@gmail.com"
        receiver = [instance.email, ]
       
        
        
        # send email
        send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=False,
            )
  


# generate reset link for password
def generate_reset_link(user):
    #encode the user id
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    #generate specific token for the user
    token = default_token_generator.make_token(user)
    reset_link = f"http://127.0.0.1:8000//set_password/{uid}/{token}/"
    return reset_link

# send email with reset link
def send_reset_link(user, reset_link):
         # email variables
            subject="Reset your password"
            message = f"""
                                Hi {user.username}, here is the link you requested to reset your password:
                                {reset_link}
                
                                
                                """
            sender = "mycolor.mine@gmail.com"
            receiver = [user.email, ]
             # send email
            send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=False,
            )


#check if the uid is valid
def is_valid_uidb64(uidb64):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    return user


