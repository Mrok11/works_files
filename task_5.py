sorted_words = []
sorted_by_alphabet_AZ = []
sorted_by_length_word = []
sorted_by_alphabet_ZA = []

with open("words.txt", "r", encoding="UTF-8") as file:
    sorted_words = file.read().split()

sorted_by_alphabet_AZ = sorted(sorted_words)
sorted_by_alphabet_ZA = sorted(sorted_words, reverse=True)
sorted_by_length_word = sorted(sorted_words, key=len)

with open("sorted_alphabetically.txt", "w", encoding="UTF-8") as file1:
    print(*sorted_by_alphabet_AZ, sep="\n", file=file1)

with open("sorted_by_length.txt", "w", encoding="UTF-8") as file2:
    print(*sorted_by_length_word, sep="\n", file=file2)

with open("sorted_reverse.txt", "w", encoding="UTF-8") as file3:
    print(*sorted_by_alphabet_ZA, sep="\n", file=file3)
