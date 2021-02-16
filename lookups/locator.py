"""
Class responsible for getting webelements.
Allows to store in one object a single webelement
or a list of webelements with the same locator.
"""
from typing import List, Union

from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

WEB_ELEMENT_TYPE = Union[WebElement, List[WebElement]]


class Locator:
    """
    Create objects which enable to get elements of pages.
    """

    def __init__(
            self,
            driver,  # type: RemoteDriver
            selector,  # type: str
            by="css_selector",  # type: str
            many=False,  # type: bool
            node=None  # type: WebElement
    ) -> None:
        """
        :param driver: a reference to the current WebDriver object
        :param selector: a selector which is used to locate an element
        :param by: a type of the selector
          Available types:
            - id
            - class_name
            - name
            - link_text
            - partial_link_text
            - tag_name
            - css_selector
            - xpath
          Default value: 'css_selector'.
          Values given as this parameter can contain space instead of
            underscore. For example, both:
              - 'css selector'
              - 'css_selector'
            are correct for the 'by' parameter.
        :param many: a switcher used to define if the current Locator
          object should look for a single or multiple elements.
        """

        self.driver = driver  # type: RemoteDriver
        self._selector = selector  # type: str
        self._by = by  # type: str
        self._many = many  # type: bool
        self._node = node or driver

    def get_when_visible(self, wait_time=15) -> WEB_ELEMENT_TYPE:
        """
        Get webelement or list of webelements when they will be visible.

        :param wait_time: number of seconds to wait
        """

        method = getattr(
            EC,
            "visibility_of_{}_located".format("all_elements" if self._many else "element")
        )
        return (get_wait(self.driver, wait_time)
                    .until(method((self._by.replace("_", " "), self._selector))))

    def get_when_clickable(self, wait_time=15) -> WEB_ELEMENT_TYPE:
        """
        Get webelement when it will be clickable.

        :param wait_time: number of seconds to wait
        """

        return (get_wait(self.driver, wait_time)
                    .until(EC.element_to_be_clickable(
                        (self._by.replace("_", " "), self._selector),
                    ))
               )

    def select_by_text(self, text) -> None:
        """
        Select option from dropdown by text
        """
        select = Select(self.get_when_clickable())
        select.select_by_visible_text(text)


def get_wait(driver, wait_time=15) -> WebDriverWait:
    """
    Get the WebDriverWait object.

    :param driver: current webdriver object
    :param wait_time: number of seconds to wait
    """

    # Avoid wait_time == 0
    wait_time = wait_time or 15
    return WebDriverWait(driver, wait_time)
