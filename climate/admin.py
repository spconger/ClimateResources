from django.contrib import admin
from .models import ContentPublisher, Media, MediaType, Institution, Person, PersonType, Location,Event, EventType, Topic

# Register your models here.
admin.site.register(MediaType)
admin.site.register(Media)
admin.site.register(ContentPublisher)
admin.site.register(Institution)
admin.site.register(Person)
admin.site.register(PersonType)
admin.site.register(Location)
admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(Topic)