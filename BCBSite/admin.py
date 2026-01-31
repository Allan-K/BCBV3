from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Songs, Events, Links, Testimonials, Gallery


# Register your models here.

admin.site.register(Songs)
admin.site.register(Events)
admin.site.register(Links)
admin.site.register(Testimonials)
admin.site.register(Gallery)

