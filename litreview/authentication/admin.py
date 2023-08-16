# Powered By M. EL-WALID EL-KHABOU
from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import User


admin.site.site_header = 'LITReview'
admin.site.site_title = 'LITReview - Interface administrateur'
admin.site.index_title = 'Interface administrateur'
admin.site.unregister(Group)


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
