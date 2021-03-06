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

from gateway.builders.authorization_builder import AuthorizationBuilder
from unittest import TestCase
from unittest.mock import patch


class TestAuthorizationBuilder(TestCase):
    BUILDER = None
    DATA = {}
    MANDATORY_FIELDS = {}

    def setUp(self):
        self.DATA = {}
        self.MANDATORY_FIELDS = {}
        self.BUILDER = AuthorizationBuilder(self.DATA, self.MANDATORY_FIELDS)

    def tearDown(self):
        del self.DATA
        del self.MANDATORY_FIELDS

    def test_create_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, AuthorizationBuilder)

    def test_build_with_account_guid(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_account_guid') as mock:
            new.add_account_guid('3383e58e-9cde-4ffa-85cf-81cd25b2423e')
        mock.assert_called_once_with('3383e58e-9cde-4ffa-85cf-81cd25b2423e')

    def test_build_with_secret_key(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_secret_key') as mock:
            new.add_secret_key('TheKey')
        mock.assert_called_once_with('TheKey')

    def test_build_with_session(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_session_id') as mock:
            new.add_session_id('TheXSession')
        mock.assert_called_once_with('TheXSession')

    def test_mandatory_and_data_fields(self):
        """Will succeed"""
        new = self.BUILDER
        new.add_account_guid('3383e58e-9cde-4ffa-85cf-81cd25b2423e')
        new.add_secret_key('UniverseSecretsKey')
        from gateway.data_sets.request_parameters import (RequestParameters, RequestParametersTypes)
        valid_fields_types = {
            RequestParameters.AUTH_DATA_ACCOUNT_GUID: RequestParametersTypes.AUTH_DATA_ACCOUNT_GUID,
            RequestParameters.AUTH_DATA_SECRET_KEY: RequestParametersTypes.AUTH_DATA_SECRET_KEY,
        }
        self.assertDictEqual(valid_fields_types, self.MANDATORY_FIELDS)
        valid_data_structure = {'secret-key': 'UniverseSecretsKey', 'account-guid': '3383e58e-9cde-4ffa-85cf-81cd25b2423e'}
        self.assertDictEqual(valid_data_structure, self.DATA)
