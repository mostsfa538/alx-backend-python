#!/usr/bin/env python3
""" Parameterize a unit test """
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ a unittest class for the utils.AccessNestedMap method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test access nested map """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test access nested map exception """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ a unittest class for the utils.get_json method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ test the utils.get_json method """
        mock_res = Mock()

        mock_res.json.return_value = test_payload
        mock_get.return_value = mock_res

        res = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ a unittest class for the utils.memoize method """

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """ test memoize """
        with patch.object(self.TestClass, 'a_method') as mock_method:
            test_instance = self.TestClass()

            test_instance.a_property()
            test_instance.a_property()

            mock_method.assert_called_once()
