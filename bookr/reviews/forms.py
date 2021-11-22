from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(min_length=3)
    search_in = forms.ChoiceField(required=False, choices=(('title': 'Title'), ('contributors': 'Contributors')))
