from selenium import webdriver
import os


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get(os.environ.get("BASE_URL"))


def after_scenario(context, scenario):
    context.driver.quit()


def before_step(context, step):
    context.step_name = step.name
