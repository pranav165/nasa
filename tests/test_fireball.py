from api.nasa_api import *
from settings import *
from hamcrest import assert_that, calling, raises
from utils.range import check_in_range

api = Nasa()

#
# def test_api_supported_version():
#     """
#     Test to verify that api version is supported
#     """
#     supported_version = str(API_SUPPORTED_VERSION)
#     res = api.get_fireball_response(params={'limit': 1})
#     assert_that(res["signature"]["version"] == supported_version)
#
#
# def test_api_response_mapper():
#     """
#     Test to verify that response order of fields. Eg first field should be date
#     """
#     res = api.get_fireball_response(params={'limit': 1})
#     assert res["fields"][0] == NasaApiResponseMapper.DATE.name.lower()
#
#
# def test_api_response_future_date():
#     """
#     Test to verify that response count is 0 for future date
#     """
#     assert_that(calling(api.get_fireball_response).with_args(params={'date-min': '2022-01-01'}),
#                 raises(NasaApiNoMatchingDataFoundError))
#
#
# def test_decimal_range_check():
#     """
#     Test to verify the utility method
#     """
#     assert check_in_range(1.5, 0, 10)
#     assert check_in_range(-1.5, 0, 10) is False
#
#
# def test_response_filter_by_location():
#     """
#     Test to verify filtering is working
#     """
#     res = api.filter_fireball_api_response(location=loc_boston)
#     assert res[-1] == 'BOSTON'
