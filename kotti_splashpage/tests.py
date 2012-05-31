from kotti.testing import FunctionalTestBase
from kotti.testing import UnitTestBase

from kotti.testing import (
    tearDown,
    testing_db_url,
    )

BASE_URL = 'http://localhost:5000'


def setUpFunctional(global_config=None, **settings):
    from kotti import main
    import wsgi_intercept.zope_testbrowser
    from webtest import TestApp

    tearDown()

    _settings = {
        'sqlalchemy.url': testing_db_url(),
        'kotti.secret': 'secret',
        'kotti.site_title': 'Test Splash Page',  # for mailing
        'kotti.populators':
            'kotti.testing._populator\nkotti_splashpage.populate',
        'mail.default_sender': 'kotti@localhost',
        'kotti.includes': 'kotti_splashpage'
        }
    _settings.update(settings)

    host, port = BASE_URL.split(':')[-2:]
    app = main({}, **_settings)
    wsgi_intercept.add_wsgi_intercept(host[2:], int(port), lambda: app)
    Browser = wsgi_intercept.zope_testbrowser.WSGI_Browser

    return dict(
        Browser=Browser,
        browser=Browser(),
        test_app=TestApp(app),
        )


class TestSplashFunctional(FunctionalTestBase):
    BASE_URL = BASE_URL

    def setUp(self, **kwargs):
        self.__dict__.update(setUpFunctional(**kwargs))

    def test_it(self):
        result = self.test_app.get('/')
        assert result.status == '200 OK'
        assert 'kotti_splashpage.renderer' in result.body


class TestSplashPage(UnitTestBase):

    def test_populate(self):
        from kotti.resources import get_root
        from kotti_splashpage import populate

        root = get_root()
        self.assertFalse(root.default_view)
        populate()
        self.assertEquals(root.default_view, 'splash-page')


class TestIncludeMe(UnitTestBase):

    def test_includeme(self):
        from pyramid.testing import setUp
        from kotti_splashpage import includeme

        config = setUp()
        includeme(config)
        views = config.introspector.get_category('views')[0]
        self.assertEquals(views['introspectable']['name'], 'splash-page')
        self.assertEquals(
            views['related'][0]['name'],
            'kotti_splashpage:templates/splash-page.pt')
