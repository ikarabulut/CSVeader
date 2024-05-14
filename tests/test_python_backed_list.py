import pytest

from data_types.python_backed_list import PythonBackedList

class TestPythonBackedList:

    def test_insert_front(self):
        my_list = PythonBackedList()
        my_list.insert_front(1)
        my_list.insert_front(2)
        my_list.insert_front(3)
        assert [3, 2, 1] == my_list.contents

    def test_insert_back(self):
        my_list = PythonBackedList()
        my_list.insert_back(1)
        my_list.insert_back(2)
        my_list.insert_back(3)
        assert [1, 2, 3] == my_list.contents

    def test_insert_preferred(self):
        my_list = PythonBackedList()
        my_list.insert_preferred(1)
        my_list.insert_preferred(2)
        my_list.insert_preferred(3)
        assert [1, 2, 3] == my_list.contents

    def test_getitem(self):
        my_list = PythonBackedList()
        my_list.insert_back("foo")
        my_list.insert_back("bar")
        my_list.insert_back("baz")

        assert "foo" == my_list[0]
        assert "bar" == my_list[1]
        assert "baz" == my_list[2]

    def test_iter(self):
        my_list = PythonBackedList()
        my_list.insert_back("foo")
        my_list.insert_back("bar")
        my_list.insert_back("baz")

        assert ["foo", "bar", "baz"] == list(iter(my_list))
