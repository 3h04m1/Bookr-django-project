from django.urls import path

from .views import BookRecordFormView, FormSuccesView


urlpatterns = [
    path('new_book_record/',BookRecordFormView.as_view(),
         name='book_record_form',),
    path('entry_success/', FormSuccesView.as_view(),
         name='form_success'),
]