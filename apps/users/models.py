import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.validators import FileExtensionValidator
from django.db.models import BooleanField, CharField, UUIDField, DateTimeField, ImageField, TextChoices, Model, \
    ForeignKey, CASCADE, EmailField, FileField, DateField, TextField, OneToOneField

from apps.users.filters import validate_file_size

from django.utils import timezone


# from users.filters import validate_file_size


class User(AbstractBaseUser, PermissionsMixin):
    class SocialNetworkAccountType(TextChoices):
        GOOGLE = 'google', 'Google'
        FACEBOOK = 'facebook', 'Facebook'

    uuid = UUIDField(default=uuid.uuid4, unique=True)
    username = CharField(max_length=25, null=True, blank=True)
    phone_number = CharField(max_length=20, unique=True)
    is_business = BooleanField(default=False)
    city = ForeignKey('ads.District', CASCADE, blank=True, null=True)
    first_name = CharField(max_length=30, null=True, blank=True)
    last_name = CharField(max_length=30, null=True, blank=True)

    photo = ImageField(upload_to='users1/', default='d/image.png')
    social_network_account_type = CharField(max_length=20, choices=SocialNetworkAccountType.choices, null=True)
    is_online = BooleanField(null=True, blank=True)

    email = EmailField(null=True, blank=True)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']


class CandidateProfile(Model):
    class Drive(TextChoices):
        A = 'a', 'A'
        B = 'b', 'B'
        C = 'c', 'C'
        D = 'd', 'D'
        BE = 'be', 'BE'
        CE = 'ce', 'CE'
        DE = 'de', 'DE'

    desired_job_title = CharField(max_length=255,
                                  help_text='Vergul bilan ajratib, tanlangan lavozimlarni kiriting. 15 tagacha qoʻshishingiz mumkin.',
                                  verbose_name='Istalgan lavozim nomi')
    desired_city = ForeignKey('ads.District', CASCADE, verbose_name='Istalgan hudud')
    cv = FileField(upload_to='user_cv/',
                   help_text="Siz shu formatlarda fayl yuklashingiz mumkin: pdf, doc, docx, odt. Maksimal o'lchami 4MB.",
                   validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'odt']),
                               validate_file_size])
    owner = OneToOneField('users.User', CASCADE)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone_number = CharField(max_length=15, unique=True)
    email = EmailField(null=True, blank=True)
    year_of_birth = CharField(max_length=4)
    name_of_educational = CharField(max_length=255, verbose_name="Ta'lim muassasasi nomi *")
    direction = CharField(max_length=255, verbose_name="Yo'nalish / Ixtisos / egallangan kasb", null=True, blank=True)
    year_of_admission = CharField(max_length=4, verbose_name='Qabul qilingan yil *')
    graduation_year = DateField(verbose_name="Bitiruv yili *", null=True, blank=True)
    studying_now = BooleanField(default=False, null=True, blank=True)
    position_name = CharField(max_length=255, verbose_name="Lavozim nomi *")
    employer = CharField(max_length=255, verbose_name="Ish beruvchi", null=True, blank=True)
    work_start_date = DateField(verbose_name="Boshlanish vaqti")
    work_end_date = DateField(verbose_name="Tugash muddati", null=True, blank=True)
    working_now = BooleanField(default=False, null=True, blank=True)
    job_duties = TextField(max_length=1500, verbose_name="Shu lavozimdagi majburiyatlarning tavsifi", null=True,
                           blank=True)
    drivers_license = CharField(max_length=20, verbose_name="Toifani tanlash yoki qo'shish", choices=Drive.choices)
    hobby = CharField(max_length=30, verbose_name="Xobbiyingiz")


class Language(Model):
    class Language(TextChoices):
        ENGLISH = 'english', 'English'
        UZBEK = 'uzbek', 'Uzbek'
        RUSSIAN = 'russian', 'Russian'

    class LanguageLevel(TextChoices):
        ADVANCED = 'advanced', 'Advanced'
        PRIMARY = 'primary', 'Primary'
        LIBERAL = 'liberal', 'Liberal'
        MEDIUM = 'medium', 'Medium'

    candidate_profile = ForeignKey('users.CandidateProfile', CASCADE)
    language = CharField(max_length=30, choices=Language.choices, verbose_name='Til')
    level_knowledge = CharField(max_length=30, verbose_name="Bilim darajasi", choices=LanguageLevel.choices)


class RecentlyViewedAds(Model):
    user = ForeignKey('users.User', CASCADE)
    ads = ForeignKey('ads.Advert', CASCADE)
    created_at = DateTimeField(auto_now=True)
