import unittest

from pyramid import testing

class TutorialViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.home()

        self.assertEqual(response.status, '302 Found')
    #
    # def test_hello(self):
    #     from .views import TutorialViews
    #
    #     request = testing.DummyRequest()
    #     inst = TutorialViews(request)
    #     response = inst.hello()
    #
    #     self.assertEqual('Hello View', response['name'])


    # def test_hello_world(self):
    #     from tutorial import hello_world
    #
    #     request = testing.DummyRequest()
    #     response = hello_world(request)
    #
    #     self.assertEqual(response.status_code, 200)
    def test_plain_without_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'No Name Provided', response.body)

    def test_plain_with_name(self):
        from .views import TutorialViews

        request = testing.DummyRequest()
        request.GET['name'] = 'Fan CX'
        inst = TutorialViews(request)
        response = inst.plain()
        self.assertIn(b'Fan CX', response.body)


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from tutorial import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    # def test_hello_world(self):
    #     res = self.testapp.get('/', status=200)
    #     self.assertIn(b'<h1>Hello World!</h1>', res.body)
    #

    # def test_home(self):
    #     res = self.testapp.get('/', status=200)
    #     self.assertIn(b'<h1>Hi Home View', res.body)
    #
    # def test_hello(self):
    #     res = self.testapp.get('/howdy', status=200)
    #     self.assertIn(b'<h1>Hi Hello View', res.body)
    #

    def test_with_name(self):
        res = self.testapp.get('/plain', status=200)
        self.assertIn(b'No Name Provided', res.body)

    def test_without_name(self):
        res = self.testapp.get('/plain?name=Fan%20CX', status=200)
        self.assertIn(b'Fan CX', res.body)