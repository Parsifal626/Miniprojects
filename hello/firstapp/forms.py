from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", max_length=15, help_text="Фио не более 15 символов")
    age = forms.IntegerField(label="Возраст клиента")
    vyb = forms.NullBooleanField(label="Поедет в Сочи?")
    email = forms.EmailField(label="Электронный адрес", help_text= "Обязательный символ - @")