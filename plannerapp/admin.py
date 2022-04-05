# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import WorkoutTime, WorkoutPlan, Workout


admin.site.register(WorkoutPlan)


@admin.register(WorkoutTime)
class WorkoutTimeAdmin(admin.ModelAdmin):
    list_display = ('workout_time_name',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = (
        'workout_name', 
        'workout_time', 
        'workout_plan', 
        'day'
    )