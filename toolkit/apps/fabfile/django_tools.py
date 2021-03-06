from __future__ import with_statement

from fabric.state import env
from fabric.api import settings

from .environment import __exec_cmd
from .server import reload_http, update_requirements
from .git_tools import git_pull


def manage(cmd):
    """
    run manage.py commands on specified role
    """
    __exec_cmd('%s/bin/python %s/manage.py %s --settings %s' % (env.role['virtualenv'],
                                                                env.role['django_root'],
                                                                cmd,
                                                                env.role['settings_param']))


def collectstatic():
    """
    runs collect static on the selected role
    """
    manage('collectstatic --noinput')


def clear_compiled_python_files():
    """
    clears compiled python files
    """
    __exec_cmd('find %s/ -name "*.pyc" -exec rm -rf {} \;' % env.role['django_root'])


def run_migrations():
    """
    runs migrations on all LOCAL_APPS
    """
    with settings(warn_only=True):
        manage('migrate')


def deploy():
    """
    deploys code to selected role  migrates db, loads initial data, installs requirements & restarts, CANNOT RUN LOCALLY
    """
    clear_compiled_python_files()
    git_pull()
    update_requirements()
    run_migrations()
    collectstatic()
    reload_http()


def soft_deploy():
    """
    runs git pull, collectstatic and restarts
    """
    clear_compiled_python_files()
    git_pull()
    collectstatic()
    reload_http()


def load_initial_data():
    """
    loads initial_fixture.json fixture
    """
    load_fixture('initial_fixture.json')


def load_fixture(fixture):
    """
    loads fixture
    """
    manage('loaddata %s' % fixture)


def django_console():
    """
    runs shell on specified role
    """
    manage('shell')
