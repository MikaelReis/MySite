<<<<<<< HEAD

=======
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17
import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
<<<<<<< HEAD


    assert response.content == b'Hello World'
=======
    assert response.content == b'Hello, world. You\'re at the blog index.'
>>>>>>> a993f214c704b874056ff7b22412a018e1702d17
