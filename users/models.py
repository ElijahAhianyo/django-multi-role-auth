from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        print(f"this is password {password}")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'mobile'
    email = models.EmailField('email', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(unique=True,validators=[phone_regex], max_length=17)
    role = models.ManyToManyField('Roles',related_name='user_role',blank=True)
    objects = UserManager()

    def __unicode__(self):
        return self.email
    
    @classmethod
    def add_role(cls,current_user,current_role):
        current_user.role.add(current_role)

    
    @classmethod
    def remove_role(cls,current_user,current_role):
        current_user.role.remove(current_role)




class Roles(models.Model):
    ROLE_CHOICES = (
      ('PATIENT', 'patient'),
      ('STAFF', 'staff'),
      ('SUPPORT', 'support'),
      ('ADMIN', 'admin'),
    )
    display = models.CharField(max_length=50,choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
      return self.display