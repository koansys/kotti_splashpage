from kotti.testing import FunctionalTestBase


class TestLogin(FunctionalTestBase):
    def test_it(self):
        assert self.browser.status == '200 OK'
        assert 'SPLASH PAGE' in self
