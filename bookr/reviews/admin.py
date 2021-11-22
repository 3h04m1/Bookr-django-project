from django.contrib import admin

from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class BookAdmin(admin.ModelAdmin):
    date_hierarchy = ('publication_date')
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'date_created')
    list_filter = ('date_created',)
    exclude = ('date_edited',)
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('creator', 'book')}),
                 ('Review Content', {'fields': ('content', 'rating')}),)

    def review_title(self, obj):
        return f"{obj.book.title} - {obj.creator}"


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
