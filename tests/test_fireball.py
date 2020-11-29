from api.nasa_api import *
from settings import *
from hamcrest import assert_that

api = Nasa()


def test_api_supported_version():
    """
    Test to verify that user has access to external Salesforce account like Z TEST AND DEMO ACCOUNT
    """
    supported_version = str(API_SUPPORTED_VERSION)
    res = api.get_fireball_response(params={'limit': 1})
    assert_that(res["signature"]["version"] == supported_version)
