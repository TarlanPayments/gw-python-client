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


class MerchantOrderBuilder(object):
    """
    Merchant data - information about merchant
    """
    # First layer of that data set
    __GENERAL_DATA_KEY = 'general-data'
    # Nested layer of general data set
    __ORDER_DATA_KEY = 'order-data'

    # Base structure of customer data
    __order_data_structure = {
        __ORDER_DATA_KEY: None
    }

    def __init__(self, __transaction_data_set):
        from gateway.utils.data_structures import DataStructuresUtils
        from gateway.data_sets.request_parameters import RequestParameters
        self.__data_structure_util = DataStructuresUtils
        self.__req_params = RequestParameters
        self.__general_data_set = __transaction_data_set
        if self.__GENERAL_DATA_KEY not in self.__general_data_set:
            self.__general_data_set[self.__GENERAL_DATA_KEY] = self.__order_data_structure

    def add_merchant_transaction_id(self, transaction_id=None):
        """
        Add merchant-side transaction ID

        Args:
            transaction_id (str): Merchant-side transaction ID
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_MERCHANT_TRANSACTION_ID: transaction_id
            }
        )

    def add_merchant_user_id(self, user_id=None):
        """
        Add merchant-side user ID

        Args:
            user_id (str): Merchant-side user ID
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_MERCHANT_USER_ID: user_id
            }
        )

    def add_merchant_order_id(self, order_id=None):
        """
        Add merchant-side order ID

        Args:
            order_id (str): Merchant-side order ID
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_ORDER_ID: order_id
            }
        )

    def add_merchant_order_description(self, description=None):
        """
        Add merchant-side order short

        Args:
            description (str): Merchant-side order short
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_ORDER_DESCRIPTION: description
            }
        )

    def add_merchant_order_meta(self, json_object=None):
        """
        Add merchant-side Key-Value order data

        Args:
            json_object (dict): Merchant-side Key-Value order data
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_ORDER_META: json_object
            }
        )

    def add_merchant_side_url(self, url=None):
        """
        Add merchant-side URL

        Args:
            url (str): Merchant-side URL
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_MERCHANT_SIDE_URL: url
            }
        )

    def add_recipient_name(self, recipient_name=None):
        """
        Add recipient name

        Args:
            recipient_name (str): Recipient name
        """
        self.__data_structure_util.add_to_dict(
            source_dict=self.__general_data_set[self.__GENERAL_DATA_KEY],
            working_dict=self.__order_data_structure,
            new_key=self.__ORDER_DATA_KEY,
            new_dict={
                self.__req_params.GENERAL_DATA_ORDER_DATA_RECIPIENT_NAME: recipient_name
            }
        )
