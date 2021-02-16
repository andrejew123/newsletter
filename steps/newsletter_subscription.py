from assertpy import assert_that
from behave import given, then, when
import datetime

import page_objects.subscribe as subscribe


@given("I am on newsletter page")
def step_impl(context):
    context.page = subscribe.SubscriptionPage(context.driver)


@when("I fill fields with {data}")
def step_impl(context, data):
    if data == "email":
        context.page.get_data(data).get_when_visible().send_keys('a975c59df3-ca60cc@inbox.mailtrap.io')
    else:
        context.page.get_data(data).get_when_visible().send_keys(data)


@when("I click to read an agreement")
def step_impl(context):
    context.page.agreement_link.get_when_clickable().click()


@when("I choose {newsletter_type} from dropdown menu")
def step_impl(context, newsletter_type):
    context.page.dropdown_menu.get_when_clickable().click()
    context.page.select_from_dropdown_menu(newsletter_type).get_when_visible().click()


@when("I enter tomorrow date to 'Ending date' field")
@when("I enter today date to 'Starting date' field")
def step_impl(context):
    context.today_date = datetime.date.today()
    context.today_date_to_string = context.today_date.strftime("%B %-d, %Y")
    context.page.start_date.get_when_clickable().click()
    context.page.choosing_today_date(context.today_date_to_string).get_when_visible()[0].click()

    if "tomorrow" in context.step_name:
        context.tomorrow_date = context.today_date + datetime.timedelta(days=1)
        context.tomorrow_date_to_string = context.tomorrow_date.strftime("%B %-d, %Y")
        context.page.end_date.get_when_clickable().click()
        context.page.choosing_today_date(context.tomorrow_date_to_string).get_when_visible()[0].click()


@when("I marked that I have read the agreement")
def step_impl(context):
    context.page.agreement_checkbox.get_when_clickable().click()


@when("I clicked 'Submit' button")
def step_impl(context):
    context.page.submit_button.get_when_clickable().click()


@when("I click OK button on confirmation modal")
def step_impl(context):
    context.page.ok_button.get_when_clickable().click()


@when("I repeat filing fields with the same data")
def step_impl(context):
    context.execute_steps("""
        When I fill all fields with correct data
        And I clicked 'Submit' button
        """)


@when("I leave all fields empty")
def step_impl(context):
    pass


@when("I fill all fields with correct data")
def step_impl(context):
    context.execute_steps("""
        When I fill fields with email
        And I fill fields with name
        And I fill fields with surname
        And I choose IT from dropdown menu
        And I enter today date to 'Starting date' field
        And I marked that I have read the agreement
        """)


@when("I fill email field with incorrect {data}")
def step_impl(context, data):
    context.page.get_data('email').get_when_visible().send_keys(data)


@then("warning about wrong email is visible")
def step_impl(context):
    (assert_that(context.page.empty_fields.get_when_visible()[0].text)
     .described_as("Checking correctness of warning message")
     .contains("Write correct email address "))


@then("information that email is already in use is visible")
def step_impl(context):
    (assert_that(context.page.email_already_in_use_warning.get_when_visible().text)
     .described_as("Checking correctnes of warning information about email already in use ")
     .contains("This e-mail is already in use. Please use different email"))


@then("modal with confirmation that user has been added to the newsletter is visible")
def step_impl(context):
    (assert_that(context.page.confirmation_modal.get_when_visible().text)
     .described_as("Checking if confirmation modal is visible")
     .contains("Successfully added to newsletter"))


@then("information about missing all fields is displayed correctly")
def step_impl(context):
    dict = {0: 'The "E-mail" field is required!', 1: 'The "First name" field is required!',
            2: 'The "Surname" field is required!', 3: 'The "newsletter type" field is required!',
            4: 'The "Start date" field is required!', 5: 'Accepting terms and condition is required!'}

    for idx, val in enumerate(context.page.empty_fields.get_when_visible()):
        assert_that(val.text).described_as("Checking the correctness of the information for user").contains(dict[idx])


@then("agreement contains all valid data")
def step_impl(context):
    (assert_that(context.page.agreement_title.get_when_visible().text)
     .described_as("Checking agreement details")
     .contains("Agreement"))


@then("information that subscription must be longer day is visible")
def step_impl(context):
    # notification should be corrected when XXX(bug number) will be resolved
    (assert_that(context.page.error_notification.get_when_visible().text)
     .described_as("Checking error notification")
     .contains("must be at least 30 days after the"))
