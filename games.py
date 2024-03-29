import random, sys


def magic_8_ball(question):
    print('What question would you like to answer?\n')
    print(f'{question.upper()} ?\n')
    messages = ['It is certain', 'It is decidedly so', 'Without a doubt',\
               'Yes ... definitely', 'You may rely on it', 'As I see it, yes',\
                'Most likely', 'Outlook good', 'Yes Signs point to yes',\
                'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now',\
                'Cannot predict now', 'Concentrate and ask again', 'Dont count on it',\
                'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    print(messages[random.randint(0, len(messages) - 1)])


def rock_paper_scissors():
    print(F'ROCK PAPER SCISSORS')

    wins = 0
    losses = 0
    ties = 0

    while True:
        print('%s wins, %s losses, %s ties' % (wins, losses, ties))
        while True:
            print('enter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move = input()
            if player_move == 'q':
                sys.exit()  # quit the program
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break
            print('choose one of the options')

        if player_move == 'r':
            print('ROCK versus...')

        if player_move == 'p':
            print('PAPER versus...')

        if player_move == 's':
            print('SCISSORS versus...')

        random_number = random.randint(1, 3)
        print(random_number)
        if random_number == 1:
            computer_move = 'r'
            print('ROCK')
        elif random_number == 2:
            computer_move = 'p'
            print('PAPER')
        elif random_number == 3:
            computer_move = 's'
            print('SCISSORS')

        if player_move == computer_move:
            print('it is a tie')
            ties += 1
        elif player_move == 'r' and computer_move == 's':
            print('you win')
            wins += 1
        elif player_move == 'p' and computer_move == 'r':
            print('you win')
            wins += 1
        elif player_move == 's' and computer_move == 'p':
            print('you win')
            wins += 1
        elif player_move == 'r' and computer_move == 'p':
            print('you lose')
            losses += 1
        elif player_move == 'p' and computer_move == 's':
            print('you lose')
            losses += 1
        elif player_move == 's' or computer_move == 'r':
            print('you lose')
            losses += 1




