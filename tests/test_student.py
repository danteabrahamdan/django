import pytest
from daytwo.models import Students
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_student():
    student = Students.objects.create(
        firstname='Example Name',
        lastname='Example Last Name',
        email='name@gmail.com',
        course='Example Name course',
        gender='Gender people'
    )

    assert student.firstname == 'Example Name'

@pytest.mark.django_db
def test_create_admin_user():
    user = User.objects.create_user(
        username='Example Name',
        email='name@gmail.com',
        password='12345678+Name'
    )
    """ user = User.objects.create_superuser(
        username='Example Name',
        email='name@gmail.com',
        password='12345678+Name'
    ) """

    assert user.is_superuser