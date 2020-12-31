from django.contrib.auth import user_logged_in
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request

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


current_user = None


@receiver(user_logged_in, sender=User)
def user_logged_in(sender, request, user, **kwargs):
    print("hello")
    global current_user
    current_user = user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    """Automatically Create A User Profile When A New User IS Registered"""
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        if instance.user_type == '0':
            root_admin = RootAdmin(user=instance)
            root_admin.save()
        elif instance.user_type == '1':
            root_mod = Rootmod(user=instance)
            profile = RootAdmin.objects.filter(user=request.user.id)[0]
            root_mod.admin = profile
            root_mod.save()
        elif instance.user_type == '2':
            company_admin = CompanyAdmin(user=instance)
            company_admin.save()
        elif instance.user_type == '3':
            company_mod = CompanyMod(user=instance)
            profile = RootAdmin.objects.filter(user=request.user.id)[0]
            company_mod.company = profile
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
