# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Publisher
from .models import Author
from .models import Book
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
