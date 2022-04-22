import pprint

message = "il est encore plus facile de juger de l'espirit d'un homme par ses question que par ses reponses"
count = {}


def counter(message):
    # this contraption below actually counts all letters and tallies them
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    pprint.pprint(count)