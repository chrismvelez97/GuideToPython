                        # Program to run Survey App
from survey import AnonymousSurvey as anonS

# Define a question, and make a survey from our imported class
question = "What language did dyou first learn to speak?"
my_survey = anonS(question)

my_survey.show_questions()
print ("Enter 'q' at any time to quit the program.")

while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_responses(response)+
