from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    resp = app.request("/Hello")
    assert_response(resp, status="404")

    resp = app.request("/")
    assert_response(resp)

    resp = app.request("/", method="POST")
    assert_response(resp, contains="Nobody")

    data = {"name": "Jason", "greeting": "Hello"}
    resp = app.request("/", method="POST", data=data)
    assert_response(resp, contains="Jason")
