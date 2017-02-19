from django.test import TestCase
#
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1, 3)


from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  # 1
        response = home_page(request)  # 2
        print(repr(response.content))
        self.assertTrue(response.content.startswith(b'<html>'))  # 3
        self.assertIn(b'<title>To-Do lists</title>', response.content)  # 4
        self.assertTrue(response.content.endswith(b'</html>'))  # 5

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
