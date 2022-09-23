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
def testListApplication_unauthenticatedUserRequest_returnsForbidden(test_user):
    # given
    client = APIClient()

    # when
    response = client.get('/applications/', format='json')

    # then
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def testListApplication_noApplicationInDb_returnEmptyList(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    # when
    response = client.get('/applications/', format='json')

    # then
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def testListApplication_oneApplicationInDb_oneApplicationInResponse(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    Application.objects.create(applicant=test_user,
                               opening='1',
                               description='some desc')

    # when
    response = client.get('/applications/', format='json')

    # then
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def testCreateApplication_unauthenticatedUserRequest_returnsForbidden(test_user):
    # given
    client = APIClient()

    # when
    response = client.post('/applications/', {'applicant': test_user.id,
                                              'opening': '1',
                                              'description': 'some desc'
                                              })

    # then
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def testCreateApplication_authenticatedUserRequest_returnSuccessful(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    # when
    response = client.post('/applications/', {'applicant': test_user.id,
                                              'opening': '1',
                                              'description': 'some desc'
                                              })

    # then
    created_application = Application.objects.get(pk=response.data['id'])
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {'id': created_application.id,
                             'applicant': test_user.id,
                             'opening': '1',
                             'status': 'IR',
                             'description': 'some desc'
                             }
    assert Application.objects.count() == 1
    assert created_application.description == 'some desc'


@pytest.mark.django_db
def testUpdateApplication_unauthenticatedUserRequest_returnsForbidden(test_user):
    # given
    client = APIClient()

    test_application = Application.objects.create(applicant=test_user,
                                                  opening='1',
                                                  description='some desc')

    # when
    response = client.put(f'/applications/{test_application.id}/',
                          {'applicant': test_user.id,
                           'opening': 1,
                           'status': 'IR',
                           'description': 'some desc'
                           })

    # then
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def testUpdateApplication_authenticatedUserRequest_updatesSuccesful(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    test_application = Application.objects.create(applicant=test_user,
                                                  opening='1',
                                                  description='some desc')

    # when
    response = client.put(f'/applications/{test_application.id}/',
                          {'applicant': test_user.id,
                           'opening': 1,
                           'status': 'IR',
                           'description': 'some other desc'
                           })

    # then
    new_application = Application.objects.get(pk=test_application.id)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['description'] == 'some other desc'
    assert new_application.description == 'some other desc'


@pytest.mark.django_db
def testRetrieveApplication_authenticatedUserRequest_updatesSuccesful(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    test_application = Application.objects.create(applicant=test_user,
                                                  opening='1',
                                                  description='some desc')

    # when
    response = client.get(f'/applications/{test_application.id}/', format='json')

    # then
    response.status_code == status.HTTP_200_OK
    assert response.data == {'id': test_application.id,
                             'applicant': test_user.id,
                             'opening': '1',
                             'status': 'IR',
                             'description': 'some desc'
                             }


@pytest.mark.django_db
def testDestroyApplication_authenticatedUser_oneApplicationInDb_operationSuccessful(test_user):
    # given
    client = APIClient()
    client.force_authenticate(test_user)

    test_application = Application.objects.create(applicant=test_user,
                                                  opening='1',
                                                  description='some desc')

    # when
    response = client.delete(f'/applications/{test_application.id}/')

    # then
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Application.objects.count() == 0
