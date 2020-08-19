HUMAN_NAME = 'human'
import string

class People(object):
    # def __init__(self,name):
    #     self.name = name

    def say_hello(self):
        with open('greetings.txt') as greet:
            t = greet.read()
        return print(t)

    def asking(self, name):
        with open('question.txt') as quest:
            t = string.Template(quest.read())
        question = t.substitute(name=name)
        return print(question)

    def thanks(self, name):
        with open('appreciation.txt') as thanks:
            t = string.Template(thanks.read())
        contents = t.substitute(name=name)
        return print(contents)


