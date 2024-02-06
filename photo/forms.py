
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import Photo, Tag, Category

class PhotoCreateForm(ModelForm):
    class Meta:
        model = Photo
        exclude = ['owner']

class TagCreateForm(ModelForm):
    class Meta:
        model = Tag

class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category

