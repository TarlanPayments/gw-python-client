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

from gateway.builders.system_data_builder import SystemDataBuilder
from unittest import TestCase
from unittest.mock import patch


class TestCommandDataBuilder(TestCase):
    BUILDER = None
    DATA = {}

    def setUp(self):
        self.DATA = {}
        self.BUILDER = SystemDataBuilder(self.DATA)

    def tearDown(self):
        del self.DATA

    def test_create_builder_instance(self):
        """Will succeed"""
        self.assertIsInstance(self.BUILDER, SystemDataBuilder)

    def test_build_with_add_user_ip(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_user_ip') as mock:
            new.add_user_ip('127.0.0.1')
        mock.assert_called_once_with('127.0.0.1')

    def test_build_with_add_x_forwarded_for_ip(self):
        """Will succeed"""
        new = self.BUILDER
        with patch.object(new, 'add_x_forwarded_for_ip') as mock:
            new.add_x_forwarded_for_ip('127.0.0.1')
        mock.assert_called_once_with('127.0.0.1')

    def test_mandatory_and_data_fields(self):
        """Will succeed"""
        new = self.BUILDER
        new.add_user_ip(cardholder_ipv4='192.168.1.70')
        new.add_x_forwarded_for_ip(cardholder_ipv4='192.168.1.70')
        valid_data_structure = {'system': {'user-ip': '192.168.1.70', 'x-forwarded-for': '192.168.1.70'}}
        self.assertDictEqual(valid_data_structure, self.DATA)
