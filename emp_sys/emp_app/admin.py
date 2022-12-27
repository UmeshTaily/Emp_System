from django.contrib import admin
from emp_app.models import Department, Employee, Role
# Register your models here.
class Emp_admin(admin.ModelAdmin):
    list_display=('first_name','last_name', 'phone', 'dept', 'role', 'date')

admin.site.register(Employee, Emp_admin)

class Dept_admin(admin.ModelAdmin):
    list_display=('name', 'location')

admin.site.register(Department, Dept_admin)

class Role_admin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Role, Role_admin)
