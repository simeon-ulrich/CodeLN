from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver


class CustomUser(AbstractUser):
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        # unique_together = ['email']
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.email)


class Badge(models.Model):
    STAR = 'Star'
    COLLECTOR = 'Collector'
    PIONEER = 'Pionneer'
    BADGE_CHOICES = [
        (STAR, 'Star'),
        (COLLECTOR, 'Collector'),
        (PIONEER, 'Pionneer'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="awarded_to")
    badge_type = models.CharField(max_length=20, choices=BADGE_CHOICES)

    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    @receiver(post_save, sender="badgesmanaging.Model3d")
    def create_badge(sender, instance, created, **kwargs):
        if created :
            from badgesmanaging.utils import check_star_badge, check_collector_badge
            print(instance.id)
            check_star_badge(instance.user.id, instance.id)
            check_collector_badge(instance.user.id)
            
    @receiver([post_save, m2m_changed ], sender="badgesmanaging.CustomUser")
    def create_badgeV2(sender, instance, created, **kwargs):
        if instance.id :
            from badgesmanaging.utils import check_pioneer_badge
            print(instance.id)
            check_pioneer_badge(instance.id, instance.date_joined)
            
    class Meta:
        verbose_name = "Badge"
        verbose_name_plural = "Badges"

    def __str__(self):
        return str(self.badge_type)


class Model3d(models.Model):
    description = models.CharField(max_length=100)
    image_link = models.FileField(
        upload_to="Images", default="default.png", null=True, blank=True
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="owner")
    views = models.IntegerField(default=0)
    
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(self.description)