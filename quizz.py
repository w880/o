import os
import slack

token = os.environ['1811741601:AAGnWursMxKSorOgvjuugS6InOhEeyCRZ4k']
questions_fp = 'data/questions.json'
su = ['lll5l', 'kartutbot'] # superuser

from trivia.trivia import Trivia
from trivia import bot

@slack.RTMClient.run_on(event='message')
def on_message(**payload):
    bot.on_message(payload, trivia)

if __name__ == '__main__':
    trivia = Trivia(token, questions_fp, su)
    trivia.client.start()
