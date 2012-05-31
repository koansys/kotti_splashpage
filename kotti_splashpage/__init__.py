from kotti.resources import get_root


def populate():
    site = get_root()
    site.default_view = 'splash-page'


def includeme(config):
    settings = config.get_settings()
    populators = settings.get('kotti.populators', [])
    if populators:
        if not populate in populators:
            ## if it is not in settings add it we let it be. If it is in populators
            ## because we *know* the user set the populators order on purpose.
            ## Otherwise we add it.
            settings['kotti.populators'].append(populate)
    else:
        settings['kotti.populators'] = [populate, ]
    config.add_view(
        name='splash-page',
        renderer='kotti_splashpage:templates/splash-page.pt',
    )
