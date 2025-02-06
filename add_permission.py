import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'AFP.settings')

import django
django.setup()

from api.models import Permission

permissions = [
    Permission(name='Create Role', code_name='role_create', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='role_read', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='role_update', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='role_delete', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='role_show', module_name='Role', description='User can show user'),
    Permission(name='Read User', code_name='user_read', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='user_update', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='user_show', module_name='User', description='User can show user'),
    Permission(name='Read Organization', code_name='organization_read', module_name='Organization', description='User can read organization'),
    Permission(name='Show Organization', code_name='organization_show', module_name='Organization', description='User can show organization'),
    Permission(name='Create Petition', code_name='petition_create', module_name='Petition', description='User can create petition'),
    Permission(name='Show Dashboard', code_name='dashboard_show', module_name='Dashboard', description='User can show dashboard'),
    Permission(name='Close Petition', code_name='petition_close', module_name='Petition', description='User can close petition'),
    Permission(name='Update Petition Detail', code_name='petition_detail_update', module_name='Petition Detail', description='User can update petition detail'),
    Permission(name='Show Daily Report', code_name='daily_report_show', module_name='Daily', description='User can show daily report'),
    Permission(name='Show Overall Report', code_name='overall_report_show', module_name='Overall', description='User can show overall report'),
    Permission(name='Create Suggestion', code_name='suggestion_create', module_name='Suggestion', description='User can create suggestion'),
    Permission(name='Read Suggestion', code_name='suggestion_read', module_name='Suggestion', description='User can read suggestion'),
    Permission(name='Update Suggestion', code_name='suggestion_update', module_name='Suggestion', description='User can update suggestion'),
    Permission(name='Delete Suggestion', code_name='suggestion_delete', module_name='Suggestion', description='User can delete suggestion'),
    Permission(name='Show Suggestion', code_name='suggestion_show', module_name='Suggestion', description='User can show suggestion'),
]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions to AFP ...")
    add_permission()
