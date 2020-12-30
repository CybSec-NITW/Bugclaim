from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from company.models import CompanyAdmin, CompanyMod
from researcher.models import Researcher
from root.models import RootAdmin, Rootmod


class User(AbstractUser):
    ROOTADMIN = '0'
    ROOTMOD = '1'
    COMPANYADMIN = '2'
    COMPANYMOD = '3'
    RESEARCHER = '4'
    USER_TYPE_CHOICES = (
        (ROOTADMIN, "Root Admin"),
        (ROOTMOD, "Root Moderator"),
        (COMPANYADMIN, "Company Admin"),
        (COMPANYMOD, "Company Moderator"),
        (RESEARCHER, "RESEARCHER"),
    )
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=RESEARCHER)

    class Meta:
        db_table = 'auth_user'

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    """Automatically Create A User Profile When A New User IS Registered"""

    if created:
        if instance.user_type == '0':
            root_admin = RootAdmin(user=instance)
            root_admin.save()
        elif instance.user_type == '1':
            root_mod = Rootmod(user=instance)
            root_mod.save()
        elif instance.user_type == '2':
            company_admin = CompanyAdmin(user=instance)
            company_admin.save()
        elif instance.user_type == '3':
            company_mod = CompanyMod(user=instance)
            company_mod.save()
        elif instance.user_type == '4':
            researcher = Researcher(user=instance)
            researcher.save()

def add_user_to_group(sender, instance: User, created: bool, **kwargs):
    try:
        if created:
            group, _ = Group.objects.get_or_create(name=instance.user_type)
            instance.groups.add(group)
            instance.save()
    except Group.DoesNotExist:
        pass


models.signals.post_save.connect(add_user_to_group, sender=User)