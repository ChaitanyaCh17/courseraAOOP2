from behave import when, then
import requests

BASE_URL = "http://localhost:5000"

@when('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.get(f"{BASE_URL}{endpoint}")

@when('I send a PUT request to "{endpoint}" with the following data')
def step_impl(context, endpoint):
    data = {row[0]: row[1] for row in context.table}
    context.response = requests.put(f"{BASE_URL}{endpoint}", json=data)

@when('I send a DELETE request to "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.delete(f"{BASE_URL}{endpoint}")

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code
