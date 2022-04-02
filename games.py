import random


def magic_8_ball(question):
    print('What question would you like to answer?\n')
    print(f'{question.upper()} ?\n')
    messages = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    print(messages[random.randint(0, len(messages) - 1)])


try:
    magic_8_ball('will i ever meet my soulmate')
except ValueError:
    KeyboardInterrupt