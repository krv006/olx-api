from django.contrib import admin

from apps.users.models import User, CandidateProfile, Language, RecentlyViewedAds


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(RecentlyViewedAds)
class RecentlyViewedAdsAdmin(admin.ModelAdmin):
    pass
