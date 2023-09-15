def word_filter():
    with open('dictionary.txt', 'r') as f1, open('pass_word.txt', 'w') as f2:
        for line in f1.readlines():
            if 4 < len(line) < 9:
                f2.write(line)

word_filter()