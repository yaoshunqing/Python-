# @Time : 2020/5/2 8:26 
# @Author : Yao
# @File : survey.py 
# @Software: PyCharm

class AnonymousSurvey():
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_questions(self):
        print(self.question)

    def stored_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


