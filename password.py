import random

NR_LETTERS = 11
NR_NUMBERS = 3
NR_SYMBOLS = 2


def random_pass():

    gen_symbols = [chr(random.randint(ord("!"), ord("/"))) for _ in range(NR_SYMBOLS)]
    gen_numbers = [chr(random.randint(ord("0"), ord("9"))) for _ in range(NR_NUMBERS)]

    amount_of_capitals = random.randint(1, NR_LETTERS // 2)

    gen_capitals = [chr(random.randint(ord("A"), ord("Z"))) for _ in range(amount_of_capitals)]
    gen_lower_case_letters = [chr(random.randint(ord("a"), ord("z"))) for _ in range(NR_LETTERS-amount_of_capitals)]

    final = gen_symbols + gen_numbers + gen_capitals + gen_lower_case_letters

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

    password += '54'  # The Favorite

    return password
