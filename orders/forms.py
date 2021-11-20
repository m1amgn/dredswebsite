from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=20, widget=forms.TextInput(attrs={'size': '30'}))
    phone = forms.CharField(label='Телефон', max_length=12, widget=forms.TextInput(attrs={'size': '30'}))