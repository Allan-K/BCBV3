from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from BCBSite.models import Songs, Testimonials, Events, Links, Gallery

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ('title', 'description', 'tune_type', 'file')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Description'}),
            'tune_type': forms.Select(attrs={'class':'form-control'}),
        }

class TestimonialsForm(ModelForm):
    class Meta:
        model = Testimonials
        fields = ('heading', 'content_text', 'image_file', 'article_created_at')

        widgets = {
            'heading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Heading'}),
            'content_text': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Description'}),
        } 

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ('heading', 'content_text', 'image_file', 'expire', 'article_created_at')

        widgets = {
            'heading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Heading'}),
            'content_text': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Description'}),
        }

class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = ('link_name', 'description')

        widgets = {
            'link_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'URL Link, must start: http://....'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Description'}),
        } 

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ('heading', 'content_text', 'image_file', 'article_created_at')

        widgets = {
            'heading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Heading'}),
            'content_text': forms.Textarea(attrs={'class':'form-control', 'rows':'4', 'placeholder':'Description'}),
        }