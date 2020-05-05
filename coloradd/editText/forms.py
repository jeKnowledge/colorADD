from django import forms
from .models import Post

class HomeForm (forms.ModelForm,forms.Form):
    contract = forms.ChoiceField(choices=[('Type',"Type of Contract"),('company',"Company/Enterprise"),('Municipality',"Municipality"),('School',"School/College"),('Hospital',"Hospital"),('Individual',"Individual"),('Other',"Other")],widget=forms.Select(attrs={'name':'option'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'name':'Name',"placeholder":"Name"}))
    email = forms.EmailField(label='E-mail',widget = forms.TextInput(attrs={'name':'Mail',"placeholder":"Email"}))
    subject = forms.ChoiceField(choices=[('Subject',"Subject matter"),('Licensing',"Licensing"),('Employment',"Employment"),('ColorADD Social',"ColorADD Social"),('Founds/Donations',"Founds/Donations"),('Other subject',"Other subject")],widget=forms.Select(attrs={'name':'option'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'name':'name',"placeholder":"Message"}))
    class Meta:
        model = Post
        fields = ('contract','name','email','subject','text')
