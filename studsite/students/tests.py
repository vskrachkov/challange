import random as r
from string import ascii_uppercase as UP

import factory
from django.test import TestCase

from .models import Group, Student


class GroupFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Group

    name = '{0}{0}-{1}{1}'.format(r.choice([x for x in UP]), r.randint(0, 9))


class StudentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Student

    first_name = factory.Faker('first_name', locale='ru_RU')
    second_name = factory.Faker('first_name', locale='ru_RU')
    last_name = factory.Faker('last_name', locale='ru_RU')
    student_ID = r.randint(10000, 99999)
    group = factory.SubFactory(GroupFactory)
    starosta = r.choice([True, False])


class GroupAndStudentTestCase(TestCase):
    fixtures = ['test_initial']

    def test_login(self):
        """Test logging to the site."""
        loggedin = self.client.login(username='test_user', password='1234qwer')
        self.assertTrue(loggedin)

    def test_create_group_and_student_in_it(self):
        """Test creating new a group and student in this group."""
        group = GroupFactory()
        student = StudentFactory()

    def test_user_add_group(self):
        loggedin = self.client.login(username='test_user', password='1234qwer')
        group_create_response = self.client.post(
            '/group/create', {'name': 'TEST-11'})
        self.assertEqual(group_create_response.status_code, 302)
