count = 0
with open("input.txt", "r", encoding="utf-8") as file:
    with open("statistics.txt", "w", encoding="utf-8") as file2:
        for line in file:
            count += 1
        file.seek(0)
        text = file.read()
        words = text.split()
        file2.write(
            f"Количество строк в тексте = {count}\nКоличество слов в тексте = {len(words)}"
        )
