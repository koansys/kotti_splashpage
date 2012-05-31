import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'kms',
    ]

tests_require = [
  'mock',
  'nose',
  'WebTest',
  'wsgi_intercept',
  'zope.testbrowser'
]

setup(name='kotti_splashpage',
      version='0.2.0',
      description="""\
      kotti_splashpage is a kotti package to setup the home page as a splash
      page. It allows you to simply set a template in your application
      deployment configuration and have a splash page.
      """,
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Koansys, LLC and contributors',
      author_email='info@koansys.com',
      url='http://github.com/koansys/kotti_splashpage',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires + tests_require,
      test_suite="kotti_splashpage",
      entry_points="""\
      """
      )
