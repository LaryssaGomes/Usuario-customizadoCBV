from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('E-mail é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        """
        UserName
            É igual a email por ser tratar no elemento usado no login
        """
        user.set_password(password)
        """
        set_password
            Criptografa a senha
        """
        user.save(using=self._bd)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        """
        extra_fields
            tem uma serie de elementos que podem ou não serem ocupador
        """
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_superuser', True) # usuario e superuser
        extra_fields.setdefault('is_staff', True) # acesso a areá administrativa

        if extra_fields.get('is_superuser') is not True: # Verificando se o usuario e super
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    foto = StdImageField('Foto', upload_to='FotoDeUsuario', variations={'thumb': (124, 124)}, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()