from django.conf import settings
from django.core.management import call_command
from pyvirtualdisplay import Display
from splinter import Browser

from toolkit.helpers.utils import snakify


def setup_test_environment(context, scenario, visible=0, use_xvfb=True):
    """
    Method used to setup the BDD test environment
     - Sets up Virtual Display
     - Sets up Browser
     - Sets window size
     - flushes cookies
     - Turn on debug(useful when capturing screenshots of the errors)
     - Sets Scenario
     - Truncates database tables

    Options:
     - visible (0 or 1) - Toggle Xephyr to view the Xvfb instance for limited debugging. 0: Off, 1: On.
     - use_xvfb (True/False) - Toggle Xvfb to run the tests on your desktop for in-depth debugging.
    """
    if use_xvfb:
        # Our virtual display to run firefox
        context.display = Display(visible=visible, size=(1920, 1080))
        context.display.start()
    # This is our base webdriver instance. It uses Firefox by default.
    context.browser = Browser()
    context.browser.driver.set_window_size(1920, 1080)
    context.server_url = context.config.server_url
    # Flushes all cookies.
    context.browser.cookies.delete()
    # Re-enables yellow screens on failure. (Normally disabled by
    # LiveServerTestCase)
    settings.DEBUG = True
    context.scenario = scenario.name
    call_command('flush', verbosity=0, interactive=False)


def save_failure_screenshot(context, step):
    if step.status == "failed":
        file_path = '%s_%s_error.png' % (snakify(context.scenario), snakify(step.name))
        context.browser.driver.save_screenshot(file_path)


def flush_context(context, scenario):
    context.browser.quit()  # Close the browser to get a fresh one for each test
    context.browser = None  # Flush browser from context
    if hasattr(context, 'display'):
        context.display.stop()  # Closes the virtual display (if it exists)
