from django import forms
from django.core.exceptions import ValidationError
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False,
                                  choices=(
                                      ("title", "Title"),
                                      ("contributor", "Contributor")
                                  ))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.add_input(Submit('', "Search"))

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


# Validation
def validate_email_domain(value):
    if value.split('@')[-1].lower() != "example.com":
        raise ValidationError("The email address must be on the domain 'example.com'.")


# Forms
class OrderForm(forms.Form):
    magazine_count = forms.IntegerField(min_value=0, max_value=80, widget=forms.NumberInput(attrs={"placeholder": "Number of magazines"}))
    book_count = forms.IntegerField(min_value=0, max_value=50, widget=forms.NumberInput(attrs={"placeholder": "Number of books"}))
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False, validators=[validate_email_domain], widget=forms.EmailInput(attrs={"placeholder": "Your company email address"}))

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["send_confirmation"] and not cleaned_data.get('email'):
            self.add_error("email","Please enter a email address to receive the confirmation message")
        elif cleaned_data.get("email") and not cleaned_data["send_confirmation"]:
            self.add_error("send_confirmation", "Please check if you want to receive a confirmation email")

        item_total = cleaned_data.get("magazine_count", 0) + cleaned_data.get("book_count", 0)

        if item_total > 100:
            self.add_error(None, "The total number of items must be 100 or less")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]
    rating = forms.IntegerField(min_value=0, max_value=5)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('', "Submit"))



class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('', "Submit"))

