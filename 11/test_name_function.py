# @Time : 2020/5/2 8:01 
# @Author : Yao
# @File : test_name_function.py 
# @Software: PyCharm

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

if __name__ == "__main__":
    #上面的判断必须要有
    unittest.main()