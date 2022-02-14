from django.test import TestCase
from model_mommy import mommy


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertTrue(str(self.service), self.service.service)


class RoleTestCase(TestCase):

    def setUp(self):
        self.role = mommy.make('Role')

    def test_str(self):
        self.assertTrue(str(self.role), self.role.role)


class TeamMemberTestCase(TestCase):

    def setUp(self):
        self.member = mommy.make('TeamMember')

    def test_str(self):
        self.assertTrue(str(self.member), self.member.name)
