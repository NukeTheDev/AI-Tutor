import openai
import datetime
import os

import json

openai.api_key = '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'


response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [
    {"role": "system", "content": "you are a quiz creation app, your answers will be formatted in a json file"},
    {"role": "user", "content": "make a 3 question quiz about elemetary level astronomy"},
    ]
)
print(response)

class storagesolutions:
    
    '''
    Storage solutions,
    
    functions housekeeping, save quiz, save chat
    '''
    def __init__(self):
        pass
    
    def housekeep(self):
        #use this function at the start of the app to create and get folders ready, it will create the necessary folders for the stuff that needs to be saved, and will check for those same folders in the future
        if os.path.exists("quizSTG") and os.path.exists("chatSTG"):
            print("folder exist")
        
        else:
            pathList = ['quizSTG', 'chatSTG']
            for i in pathList:
                path = os.path.join(i)
                os.mkdir(path)
            
    def saveQuiz(self, subject, grade, response):
        #will save output from AI in a json file, parsing could be necesary, naming conventions for the files are up to change.
        file_name = str(subject) + "quiz" + str(grade) #file name, could add datetime module to name the files in a more personalized manner
        file_path = file_name + ".json"
        with open(file_path, 'w') as fp:
            json.dump(response, fp)
            os.path.dirname("quizSTG")
            fp.close()
        
    def saveChat(self, chat, subject, grade):
        #
        file_name = 'chat' + str(subject) + str(grade)
        file_path = file_name + ".txt"
        with open(file_path, "w") as fp:
            os.path.dirname("chatSTG")
            fp.write(chat)
            fp.close()