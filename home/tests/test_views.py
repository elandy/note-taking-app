import pytest
from django.contrib.auth.models import User


def test_home_endpoint_returns_welcome_page(client):
    response = client.get(path='/')
    assert response.status_code == 200
    assert "Welcome to SmartNotes!" in str(response.content)


def test_signup_endpoint_returns_form_for_unauthenticated_user(client):
    response = client.get(path='/signup')
    assert response.status_code == 200
    assert "home/register.html" in response.template_name


@pytest.mark.django_db
def test_signup_endpoint_redirects_authenticated_user(client):
    """
    When a user is authenticated and try to access the
    signup page they are redirected to the list of their notes.
    """
    user = User.objects.create_user('Clara', 'clara@asasas.com', 'password')
    client.force_login(user)

    response = client.get(path='/signup', follow=True)  # follow=True to go to the redirect
    assert 200 == response.status_code
    assert "notes/notes_list.html" in response.template_name
