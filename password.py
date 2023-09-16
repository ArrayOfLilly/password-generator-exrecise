import random


def random_pass():
    num_letters = 11
    num_symbols = 2
    num_numbers = 3

    gen_symbols = ""
    for s in range(0, num_symbols):
        gen_symbols += chr(random.randint(ord("!"), ord("/")))

    gen_numbers = ""
    for n in range(0, num_numbers):
        gen_numbers += chr(random.randint(ord("0"), ord("9")))

    gen_letters = ""
    if num_letters > 0:
        amount_of_capitals = random.randint(1, num_letters // 2)

        for l in range(0, amount_of_capitals):
            gen_letters += chr(random.randint(ord("A"), ord("Z")))

        for l in range(0, num_letters - amount_of_capitals):
            gen_letters += chr(random.randint(ord("a"), ord("z")))

    final = [*(gen_symbols + gen_numbers + gen_letters)]
    random.shuffle(final)
    password = "".join(final)
    return password


def memorable():
    word_list = open("pass_word.txt").readlines()
    password = ""
    for _ in range(3):
        ind = random.randint(0, len(word_list) - 1)
        chosen_word = word_list[ind].strip().title()
        password += chosen_word + "-"
    password += '53'
    return password
