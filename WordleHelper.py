from termcolor import colored


def words_containing(bank, letter):
    temp={}
    for word in bank:
        if letter in word:
            temp[word]=bank[word]
    return temp


def words_not_containing(bank, letter):
    temp = {}
    for word in bank:
        if letter not in word:
            temp[word]=bank[word]
    return temp


def words_containing_letter_at_index(bank, letter, index):
    temp = {}
    for word in bank:
        if word[index] == letter:
            temp[word]=bank[word]
    return temp


def words_not_containing_letter_at_index(bank, letter, index):
    temp = {}
    for word in bank:
        if word[index] != letter:
            temp[word]=bank[word]
    return temp


def overall_frequency(bank):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for word in bank:
        for letter in alphabet:
            if letter in word:
                alphabet[letter] += 1
    return alphabet


def frequency(bank, index):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}

    for word in bank:
        for letter in alphabet:
            if letter == word[index]:
                alphabet[letter] += 1
    return alphabet


def sorted_dictionary(dic):
    # list containing tuples. (key, value
    sorted_list = sorted(dic.items(), key=lambda x: x[1])
    rank_value = {}
    for i in range(len(sorted_list)):
        for letter in dic:
            if dic[letter] == sorted_list[i][1]:
                rank_value[letter] = i
    return rank_value


def score(word,dictionaries):
    count = 0
    for index in range(5):
        count += dictionaries[index][word[index]]
    return count


def scored_words(bank,dictionaries):
    word_score_dict = {}
    scored = open("scored.txt", "w")
    for word in bank:
        word_score_dict[word] = score(word,dictionaries)
        # print(word + ": " + str(word_score_dict[word]))
    for word in word_score_dict.keys():
        # scored.write("%s, %s\n" % (word, word_score_dict[word]))
        scored.write(word + " "+ str(word_score_dict[word])+"\n")

    scored.close()
    return word_score_dict

def min_to_max(scored_bank):
    sorted_values = sorted(scored_bank.values())
    min_max={}
    for value in sorted_values:
         for key in scored_bank:
             if scored_bank[key]== value:
                 min_max[key]=scored_bank[key]

    return min_max



################################ Code Already Run To Generate a Scored Word Bank #######################################

five = open("five.txt", "r")
bank = five.read()
bank = bank.split()
#
# # Overall
# overall_fre = overall_frequency(bank)
# overall_rank = sorted_dictionary(overall_fre)
#
# # 1 Letter
# fre0 = frequency(bank, 0)
# rank0 = sorted_dictionary(fre0)
# # 2 Letter
# fre1 = frequency(bank, 1)
# rank1 = sorted_dictionary(fre1)
# # 3 Letter
# fre2 = frequency(bank, 2)
# rank2 = sorted_dictionary(fre2)
# # 4 Letter
# fre3 = frequency(bank, 3)
# rank3 = sorted_dictionary(fre3)
# # 5 Letter
# fre4 = frequency(bank, 4)
# rank4 = sorted_dictionary(fre4)
#
# dictionaries = [rank0, rank1, rank2, rank3, rank4]
#
# scored_bank = scored_words(bank,dictionaries)
########################################################################################################################

# five = open("five.txt", "r")
# bank = five.read()
# bank = bank.split()
#
#
# fre0 = frequency(bank, 0)
# rank0 = sorted_dictionary(fre0)
#
# for word in rank0:
#     print(word+": "+str(rank0[word]))


ranked_bank = {}
a_file = open("scored.txt")
for line in a_file:
    key, value = line.split()
    ranked_bank[key] = int(value)
    # print(key+":"+str(ranked_bank[key]))

paired_down={}
for word in ranked_bank:

    if int(ranked_bank[word])>60:
        paired_down[word]=ranked_bank[word]

ranked = min_to_max(paired_down)

word = "     "
count = 1
while count < 7:
    guess = input("\n\nGuess "+str(count)+":  ")
    scored = input("How did "+guess+" score: ")
    for i in range(5):
        if scored[i] == "G":
            ranked = words_containing_letter_at_index(ranked, guess[i],i)
        elif scored[i] == "Y":
            ranked = words_not_containing_letter_at_index(ranked, guess[i], i)
            ranked = words_containing(ranked, guess[i])
        else:
            ranked = words_not_containing(ranked, guess[i])

    ranked = min_to_max(ranked)
    for word in ranked:
        print(word+": "+str(ranked[word]))

    count += 1










