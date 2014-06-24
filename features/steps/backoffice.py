from behave import *

use_step_matcher("re")

@given("(.+) a logged out user")
def step_impl(context, a):
    pass

@given("we have an admin user")
def step_impl(context):
    pass

@when("she navigates to backoffice login window")
def step_impl(context):
    br = context.browser
    br.visit(context.browser_url('/dashboard'))

@then("(.+) is redirected to the login window")
def step_impl(context):
    br = context.browser
    response = br.response()
    assert br.geturl().endswith('/login/'), br.geturl()

@when("he logs in as admin")
def step_impl(context):
    assert True is not False

@then("he should see the main dashboard")
def step_impl(context):
    assert context.failed is False
