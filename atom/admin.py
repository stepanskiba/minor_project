from django.contrib import admin
from .models import UserModels, TaskModels, SolutionModels, ServiceModels
from .models import ScheduleTopicModels
# Register your models here.

admin.site.register(UserModels)
admin.site.register(TaskModels)
admin.site.register(SolutionModels)
admin.site.register(ServiceModels)
admin.site.register(ScheduleTopicModels)