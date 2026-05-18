from django.contrib import admin
from .models import Project, Skill, Experience, Education, Certification, Profile

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(Profile)