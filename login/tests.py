from django.test import TestCase
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from login.models import InternalUser,ExternalUser
from django.contrib.auth.models import User

# Create your tests here.
class PermissionTest(TestCase):
    def test_give_user_permission_to_access_page(self):
        content_type = ContentType.objects.get_for_model(InternalUser)
        permission = Permission.objects.create(codename='can_view_page',name='Can view page',content_type=content_type,)
        user2 = User.objects.create_user(username='john',email='johnlennon@beatles.com',password='iamironman')
        self.assertIs(user2.has_perm('login.can_view_page'), False)
        user2.user_permissions.add(permission)
        user2.save()
        user2 = User.objects.get(username='john')
        self.assertIs(user2.has_perm('login.can_view_page'), True)
