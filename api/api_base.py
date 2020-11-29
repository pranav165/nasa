# Base class for API calls . Here we implement the HTTP methods and their handeling using requests module
import requests
from requests import ReadTimeout
from requests.exceptions import ConnectionError
from retry import retry
from settings import API_TIMEOUT


class RaiseStatusException(Exception):
    pass


class CommonAPIBase:
    response_ok = 200

    @retry((ReadTimeout, RaiseStatusException, ConnectionError), tries=3, delay=2)
    def execute_request(self, method, headers, verify=False, timeout=API_TIMEOUT, *args, **kwargs):
        try:
            if method == 'POST':
                self.response = requests.post(headers=headers, verify=verify, timeout=timeout, *args, **kwargs)
            elif method == 'GET':
                self.response = requests.get(headers=headers, verify=verify, timeout=timeout, *args, **kwargs)
            elif method == 'DELETE':
                self.response = requests.delete(headers=headers, verify=verify, timeout=timeout, *args, **kwargs)
            elif method == 'PUT':
                self.response = requests.put(headers=headers, verify=verify, timeout=timeout, *args, **kwargs)

            if self.response.status_code in [502, 503, 504]:
                raise RaiseStatusException(
                    "Retrying API call as it returned the status code as {}".format(self.response.status_code))

            return self.response

        except ReadTimeout:
            raise ReadTimeout(
                "{} call for {} resulted in timeout error after {} seconds. Retrying API call".format(method,
                                                                                                      kwargs["url"],
                                                                                                      timeout))


class ApiBase(CommonAPIBase):
    def __init__(self):
        self.common_headers = {"Content-Type": "application/json"}

    def post(self, headers=None, *args, **kwargs):
        if headers is None:
            headers = self.common_headers
        return self.execute_request(method='POST', headers=headers, *args, **kwargs)

    def get(self, headers=None, *args, **kwargs):
        if headers is None:
            headers = self.common_headers
        return self.execute_request(method='GET', headers=headers, *args, **kwargs)

    def delete(self, headers=None, *args, **kwargs):
        if headers is None:
            headers = self.common_headers
        return self.execute_request(method='DELETE', headers=headers, *args, **kwargs)

    def put(self, headers=None, *args, **kwargs):
        if headers is None:
            headers = self.common_headers
        return self.execute_request(method='PUT', headers=headers, *args, **kwargs)
