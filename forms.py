from django.contrib.auth.forms import UserCreationForm

from .models import CustomUsuario

class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone','email', 'foto')
        labels = {'username':'Username/E-mail'}
        print('form1')
    
     def save(self, commit=True):
         print('form2')
         user = super().save(commit=False)
         user.set_password(self.cleaned_data['password1'])
         user.email = self.cleaned_data['username']#acesso ao objeto
         if commit:
             user.save()
         return user

