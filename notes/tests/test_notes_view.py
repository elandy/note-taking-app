import pytest
from django.contrib.auth.models import User
from notes.models import Notes
from notes.tests.factories import UserFactory, NoteFactory


@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.force_login(user)
    return user


@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client, logged_user):
    note = NoteFactory(user=logged_user)
    note2 = NoteFactory(user=logged_user)

    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content = str(response.content)
    assert note.title in content
    assert note2.title in content
    assert 2 == content.count('<h3>')


@pytest.mark.django_db
def test_list_endpoint_only_list_notes_from_authenticated_users(client, logged_user):
    jon = User.objects.create_user('Jon', 'Jon@asasas.com', 'password')
    jons_note = NoteFactory(user=jon)

    client.force_login(logged_user)
    note = NoteFactory(user=logged_user)
    note2 = NoteFactory(user=logged_user)

    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    content = str(response.content)
    assert note.title in content
    assert note2.title in content
    assert jons_note.title not in content
    assert 2 == content.count('<h3>')



@pytest.mark.django_db
def test_create_endpoint_receives_form_data(client, logged_user):
    form_data = {'title': 'An impressive Django title', 'note': 'A really interesting text'}

    response = client.post(path='/smart/notes/new', data=form_data, follow=True)

    assert 200 == response.status_code
    assert 'notes/notes_list.html' in response.template_name
    assert 1 == logged_user.notes.count()
    assert "An impressive Django title" == logged_user.notes.first().title