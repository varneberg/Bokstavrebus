import random


def shuffle(s):
    char_list = list(s)
    random.shuffle(char_list)
    new_s = ''.join(char_list)
    return new_s

def solve():
    s = input("Hvilke bokstaver er opgitt?\n").lower()
    while True:
        new_word = shuffle(s)
        print(new_word)
        with open("ordlister/ordliste_snl_fellesord.txt", 'r') as fp:
            filecontent = fp.readlines()
            for line in filecontent:
                process(line)
                #line = line.strip()
                if new_word == line:
                    return new_word




print(solve())