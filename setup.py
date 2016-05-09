from setuptools import setup
setup(
    # Metadata for PyPI; nice to have but not required
    name="cce_toolkit",
    version="1.4.7",
    description='A collection of tools for use in CCE-IT projects',
    author='CCE Devs',
    license='All Rights Reserved',
    # I don't think this url is required either, but it's nice to have
    url='ssh://code.ce.ou.edu/var/git/cceitdev/cce_toolkit.git',
    packages=['toolkit'],
    include_package_data=True,
    package_data={'toolkit': ['*.py','mixins/*.py',
                              'fabfile/*.py',
                              'breadcrumbs/*.py',
                              'breadcrumbs/middleware/*.py',
                              'breadcrumbs/templates/*.html',
                              'breadcrumbs/templatetags/*.py',
                              'templatetags/*.py',
                              'templates/*.html',
                              'templates/comments/*.html',
                              'templates/form_fragments/*.html',
                              'templates/registration/*.html',
                              'static/toolkit/*.js',
                              'static/toolkit/*.css',
                              'static/*.js',
                              'static/*.css',
                              'bdd/*.py']},
    zip_safe=False,  # important, forces it to install as directories and not .zip
)

