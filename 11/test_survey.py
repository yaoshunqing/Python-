# @Time : 2020/5/2 8:41 
# @Author : Yao
# @File : test_survey.py 
# @Software: PyCharm

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Japanese']

    def test_store_single_response(self):
        #测试方法要用test_开头
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        self.my_survey.stored_response('English')

        self.assertIn(self.responses[0], self.my_survey.responses[0])

    def test_store_three_response(self):
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Mandarin', 'Japanese']
        for response in self.responses:
            self.my_survey.stored_response(response)
        # for response in self.responses:

        self.assertEqual(self.responses, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
