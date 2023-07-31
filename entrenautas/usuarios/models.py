from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre_completo, password=None):
        if not email:
            raise ValueError('El campo Email es obligatorio')
        email = self.normalize_email(email)
        usuario = self.model(email=email, nombre_completo=nombre_completo)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre_completo, password):
        usuario = self.create_user(email, nombre_completo, password)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    nombre_completo = models.CharField(_('nombre completo'), max_length=255, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre_completo']

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_full_name(self):
        return self.nombre_completo

    def get_short_name(self):
        return self.nombre_completo

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
