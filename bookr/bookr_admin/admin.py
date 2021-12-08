
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.contrib.auth.models import Permission

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"


    def each_context(self, request):
        context = super().each_context(request)
        context['username'] = request.user.username
        user = request.user
        perms = list(user.get_user_permissions())
        context['perms'] = perms
        return context

    def get_urls(self):
        urls = super().get_urls()
        url_patterns = [
            path('admin_profile/', self.admin_view(self.profile_view))
        ]
        return url_patterns + urls

    def profile_view(self, request):
        request.current_app = self.name
        context = self.each_context(request)
        return TemplateResponse(request, "admin/admin_profile.html", context)


