found_word = input("Введите слово для поиска: ").lower()
count = 0
num_string_dict = []

with open("text.txt", "r", encoding="utf-8") as file:
    for i, line in enumerate(file, 1):
        words_in_line = (
            line.replace("!", "").replace("?", "").replace(",", "").lower().split()
        )
        if found_word in words_in_line:
            occurrences = words_in_line.count(found_word)
            count += occurrences
            num_string_dict.append(i)

with open("search_results.txt", "w", encoding="utf-8") as file:
    if count > 0:
        print("Слово найдено!")
        print(f"Слово '{found_word}' встречается {count} раз.")
        print(f"Слово встречается в строках: {num_string_dict}.")
        file.write(
            f"Слово найдено!\nСлово '{found_word}' встречается {count} раз.\nСлово встречается в строках: {num_string_dict}."
        )
    else:
        print("Слово не найдено!")
