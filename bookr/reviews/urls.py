from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views, api_views

router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("book/<int:pk>/", views.book_details, name="book_details"),
    path("books/<int:pk>/media", views.book_media, name="book_media"),
    path("books/<int:book_pk>/reviews/new/", views.review_edit, name="review_create"),
    path(
        "books/<int:book_pk>/reviews/<int:review_pk>/",
        views.review_edit,
        name="review_edit",
    ),
    path("search", views.book_search, name="book_search"),
    path("example-form", views.example_form, name="example_form"),
    path("publishers/new", views.publisher_edit, name="publisher_create"),
    path("publishers/<pk>", views.publisher_edit, name="publisher_edit"),
    path("", views.index),
    path('api/', include((router.urls, 'api'))),
    path('api/login/', api_views.Login.as_view(), name='login')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
