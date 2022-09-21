import pytest
from rest_framework import status
from rest_framework.test import APIClient

from jobapp.models import Application


@pytest.mark.django_db
@pytest.fixture(scope='function')
def test_user(django_user_model):
    return django_user_model.objects.create(email='test@user.com',
                                            first_name='test',
                                            last_name='user')


@pytest.mark.django_db
def testListApplication_noApplicationInDb_returnEmptyList(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    # when
    response = client.get('/applications/', format='json')

    # then
    assert len(response.data) == 0


@pytest.mark.django_db
def testListApplication_oneApplicationInDb_oneApplicationInResponse(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    Application.objects.create(applicant=test_user,
                               opening='1',
                               selected=False,
                               description='some desc')

    # when
    response = client.get('/applications/', format='json')

    # then
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
