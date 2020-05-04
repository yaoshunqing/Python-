# @Time : 2020/5/2 8:30 
# @Author : Yao
# @File : language_survey.py 
# @Software: PyCharm
from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.stored_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()


