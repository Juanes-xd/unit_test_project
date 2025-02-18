from django.urls import reverse, resolve
from courses.urls import urlpatterns


class TestUrls:
    # Test para la url detail
    def test_details_url(self):
        # construimos la url a partir de su definicion
        path = reverse('courses:detail', args=[1])
# ejecutamos la url
        resolver = resolve(path)
# verificamos que el nombre de la url es el correcto
        assert resolver.url_name == 'detail'
# verificamos los argumentos que se pasaran a la vista
        assert resolver.kwargs == {'pk': '1'}
