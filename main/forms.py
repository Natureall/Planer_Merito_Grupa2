from django import forms

class KontaktForm(forms.Form):
    imie = forms.CharField(label='Imię i nazwisko', max_length=100)
    email = forms.EmailField(label='Adres e-mail')
    temat = forms.CharField(label='Temat', max_length=200)
    wiadomosc = forms.CharField(label='Wiadomość', widget=forms.Textarea)
