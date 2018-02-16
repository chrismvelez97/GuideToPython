                        # Testing classes

class AnonymousSurvey():
    '''Collects anonymous answers to a survery question'''
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_questions(self):
        '''Show survey questions'''
        print (self.question)

    def store_responses(self, new_response):
        '''Store a single response to the survey'''
        self.responses.append(new_response)

    def show_results(self):
        print ("Survey results:")
        for response in self.responses:
            print("- " + response)


survey = AnonymousSurvey("Where do you live?")
survey.show_questions()
