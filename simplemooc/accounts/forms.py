from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User # import original usando a tabela de user.
from django.contrib.auth import get_user_model

User = get_user_model()

# Classe utilizada para Form com o Model original do Django

# class RegisterForm(UserCreationForm):

#     email = forms.EmailField(label='E-mail', required=False)

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError('Já existe usuário com este e-mail')
#         return email

#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit: 
#             user.save()
#         return user 

class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail', required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError(
            'Nenhum usuário cadastrado com este e-mail'
        )


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de Senha', widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']



class EditAccountForm(forms.ModelForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk) 
        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com este e-mail')
        return email
    
    class Meta:
        model = User
        #fields = ('username','email', 'first_name', 'last_name')
        fields = ('username','email')
