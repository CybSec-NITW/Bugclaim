from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


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


class RootAdmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rootadmin')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'rootadmin'


class Rootmod(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rootmod')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'rootmoderator'


class CompanyAdmin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='companyadmin')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'companyadmin'


class CompanyMod(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='companymod')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'companymoderator'


class Researcher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, max_length=100, default="")
    country = models.CharField(max_length=20, blank=True, default="")
    facebook_url = models.URLField(blank=True, default="")
    twitter_handler = models.CharField(max_length=40, blank=True, default="")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username

    class Meta:
        db_table = 'researcher'


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
