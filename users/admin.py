from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import User

# Register your models here.
class MyUserChangeForm(UserChangeForm):
    """User 情報を変更するフォーム"""
    class Meta:
        model = User
        fields = '__all__' # 全ての情報を変更可能

class MyUserCreationForm(UserCreationForm):
    """User を作成するフォーム"""
    class Meta:
        model = User
        fields = ('email',) # email とパスワードが必要

class MyUserAdmin(UserAdmin):
    """カスタムユーザーモデルの Admin"""
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'username',  'password1', 'password2'),
        }),
    )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('email',)

admin.site.register(User, MyUserAdmin)