# The MIT License
#
# Copyright (c) 2017 Tarlan Payments.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


class AuthorizationBuilder(object):
    def __init__(self, __client_auth_data_set, __client_mandatory_fields):
        from gateway.data_sets.request_parameters import (
            RequestParameters,
            RequestParametersTypes
        )
        self.__data_sets = RequestParameters
        self.__data_types = RequestParametersTypes
        self.__auth_mandatory_fields = __client_mandatory_fields
        self.__auth_data_set = __client_auth_data_set

    def add_account_guid(self, guid=None):
        """
        Tarlan Payments Merchant Account GUID.

        Args:
            guid (str): Tarlan Payments Merchant Account GUID.
        """
        self.__auth_mandatory_fields[self.__data_sets.AUTH_DATA_ACCOUNT_GUID] = self.__data_types.AUTH_DATA_ACCOUNT_GUID
        self.__auth_data_set[self.__data_sets.AUTH_DATA_ACCOUNT_GUID] = guid

    def add_secret_key(self, value=None):
        """
        Tarlan Payments Merchant Password

        Args:
            value (str): Tarlan Payments Merchant Password
        """
        self.__auth_mandatory_fields[self.__data_sets.AUTH_DATA_SECRET_KEY] = self.__data_types.AUTH_DATA_SECRET_KEY
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = value

    def add_session_id(self, id_value=None):
        """
        Tarlan Payments Gateway Session ID

        Args:
            id_value (str): Tarlan Payments Gateway Session ID
        """
        self.__auth_data_set[self.__data_sets.AUTH_DATA_SECRET_KEY] = id_value
