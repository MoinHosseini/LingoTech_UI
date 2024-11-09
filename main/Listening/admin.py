from django.contrib import admin
from .models import Answers,check_table,flow_chart,Steps
# Register your models here.
admin.site.register(Answers)
admin.site.register(check_table)
admin.site.register(flow_chart)
admin.site.register(Steps)