from kotti.resources import get_root

DEFAULT_RENDERER = 'kotti_splashpage:templates/splash-page.pt'


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
    renderer = settings.get(
        'kotti_splashpage.renderer',
        DEFAULT_RENDERER)
    config.add_view(
        name='splash-page',
        renderer=renderer,
    )
    ## why override for one template?
    # for override in [a.strip()
    #                  for a in settings.get('kotti_splashpage.asset_overrides', '').split()
    #                  if a.strip()]:
    #     config.override_asset(
    #         to_override='kotti_splashpage',
    #         override_with=override)
