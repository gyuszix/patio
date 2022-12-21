def nao_quest():
    while True:
        x = input('What gets bigger the more you take away?\nfirst word is \'a\'\n')
        if x == 'hole':
            print('Among the Ties')
            break


def nao_quest_part_2():
    while True:
        x = input('What single hand is worth most in Riichi Mahjong\nSingle word, romaji\n')
        if x == 'yakuman':
            for i in range(77824, 77928, 1):
                print(chr(i), end=' ')
            break
