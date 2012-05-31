from kotti.resources import get_root


def populate():
    site = get_root()
    site.default_view = 'splash-page'


def includeme(config):
    config.add_view(
        name='splash-page',
        renderer='kotti_splashpage:templates/splash-page.pt',
    )
