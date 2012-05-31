kotti_splashpage README
=======================

Description
-----------

`kotti_splashpage is a kotti package to setup the home page as a splash page. It
`allows you to simply set a template in your application deployment
`configuration and have a splash page.

Installation
------------

easy_install, pip, setup.py install or whatever

add `kotti_splashpage` to `pyramid.includes` and a template path to
`kotti_splashpage.renderer` something like::

    pyramid.includes =
        ...
        kotti_splashpage

And then add an override directory::
    kotti_splashpage.renderer = mypackage:templates/atemplate.pt

NB: `kotti_splashpage.includeme` adds a populate function to set the site's default view. If you
are adding several populate functions in `kotti.populators` be aware that you
may need to manually include `kotti_splashpage.populate` to control order of the
populators.
