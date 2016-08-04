from django import forms
from .models import Beliefs, Vari, Org, NewsFeed, Search


class PostForm(forms.ModelForm):

    class Meta:
        model = Beliefs
        fields = ('title', 'text',)


class OrgForm(forms.ModelForm):

    class Meta:
        model = Org
        fields = ('name', 'info',)


class SearchOrgForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('search_input',)


class CSInputForm(forms.ModelForm):

    class Meta:
        model = Vari
        fields = ('value', 'type1',)
        widgets = {
            'value': forms.fields.TextInput(attrs={'placeholder': ' Enter a number'}),
            'type1': forms.fields.TextInput(attrs={'placeholder': "Enter 'one', 'two', or something else"})
        }


class NewsForm(forms.ModelForm):

    class Meta:
        model = NewsFeed
        fields = ('title', 'text', 'published_date', 'image',)
