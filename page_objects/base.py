"""
Abstract class for page objects, with methods common
for all pages' classes.
"""
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver


class BasePage:
    """
    A class from which all page objects should inherit.

    An abstract class - do not create its instances.
    """

    def __init__(self, driver) -> None:
        """
        This constructor should be only called from inherited
        classes, in theirs constructors.

        :param driver: a reference to the current WebDriver object
        """

        self.driver = driver  # type: RemoteDriver
