import os.path
import shutil
import platform


def get_os():
    """
    Return OS of system
    """
    os = platform.system()
    return os


def is_app_present():
    os = get_os()
    if 'window' in os.casefold():
        if shutil.which("scoop") is None:
            raise Exception("scoop app is not install to generate allure report."
                            "Please visit https://docs.qameta.io/allure/ for details")
        else:
            print("Environment is already set")

is_app_present()
