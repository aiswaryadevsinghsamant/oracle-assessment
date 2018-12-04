import unittest
from assessment import stringClean, maxBlock, reorderBlock, app
from http import HTTPStatus
import sys


class TestAssessment(unittest.TestCase):

    def test_stringCleanForEmptyString(self):
        ip_data = ''
        expected_rslt = None
        rslt = stringClean(ip_data)
        self.assertEqual(expected_rslt, rslt)

    def test_stringCleanForValidString(self):
        ip_data = 'yyzzza'
        expected_rslt = 'yza'
        rslt = stringClean(ip_data)
        self.assertEqual(expected_rslt, rslt)

        ip_data = 'abbbcdd'
        expected_rslt = 'abcd'
        rslt = stringClean(ip_data)
        self.assertEqual(expected_rslt, rslt)

        ip_data = 'Hello'
        expected_rslt = 'Helo'
        rslt = stringClean(ip_data)
        self.assertEqual(expected_rslt, rslt)

    def test_maxBlockForEmptyString(self):
        ip_data = ''
        expected_rslt = 0
        rslt = maxBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)

    def test_maxBlockForValidString(self):
        ip_data = 'hoopla'
        expected_rslt = 2
        rslt = maxBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)

        ip_data = 'abbCCCddBBBxx'
        expected_rslt = 3
        rslt = maxBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)

    def test_reorderBlockForEmptyString(self):
        ip_data = ''
        expected_rslt = None
        rslt = reorderBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)

    def test_reorderBlockForValidString(self):
        ip_data = 'bbAAccAadF'
        expected_rslt = 'AAAabbccdF'
        rslt = reorderBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)

        ip_data = 'hoopla'
        expected_rslt = 'ahloop'
        rslt = reorderBlock(ip_data)
        self.assertEqual(expected_rslt, rslt)


    #API TEST CASE
    def test_invoke_function_api_invalid_function(self):
        test_app = app.test_client()
        func_name = 'inValidFunc'
        func_val = 12234
        expect_rslt = 'Invalid Request for method {}, invoked for val {}'.format(func_name, func_val)
        header = {}
        header['func_name'] = func_name
        header['func_val'] = func_val
        response = test_app.get("/invoke-function", headers=header)
        self.assertEqual(response._status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.data.decode(sys.getdefaultencoding()), expect_rslt)

    def test_invoke_function_api_valid_function(self):
        test_app = app.test_client()
        func_name = 'stringClean'
        func_val = 'yyzzza'
        expect_rslt = 'yza'
        header = {}
        header['func_name'] = func_name
        header['func_val'] = func_val
        response = test_app.get("/invoke-function", headers=header)
        self.assertEqual(response._status_code, HTTPStatus.OK)
        self.assertEqual(response.data.decode(sys.getdefaultencoding()), expect_rslt)

        func_name = 'maxBlock'
        func_val = 'hoopla'
        expect_rslt = 2
        header = {}
        header['func_name'] = func_name
        header['func_val'] = func_val
        response = test_app.get("/invoke-function", headers=header)
        self.assertEqual(response._status_code, HTTPStatus.OK)
        self.assertEqual(int(response.data.decode(sys.getdefaultencoding())), expect_rslt)