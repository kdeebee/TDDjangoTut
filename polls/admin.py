# The Poll app still isn't available via the admin site.
# That's because the Django admin site doesn't automatically contain every model you define -
# you need to tell it which models you want to be able to administer.
#
# To do that, we just need to create a new file with the following
# three lines inside the polls app called, polls/admin.py:

from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
