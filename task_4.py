alfavit = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
up = False
result = ""
new_place = 0
place = 0
letter = ""

try:
    with open("secret.txt", "r", encoding="UTF-8") as file1:
        text_secret = file1.read()

        for i in text_secret:
            if i.islower():
                up = True

            if i.upper() in alfavit:
                i = i.upper()
                place = alfavit.find(i)
                new_place = place + 3
                letter = alfavit[new_place]

            else:
                result += i

            if up:
                letter = letter.lower()
                up = False
                result += letter
                letter = ""

            else:
                result += letter
                letter = ""

    with open("encrypted.txt", "w", encoding="UTF-8") as file2:
        file2.write(result)

    result = ""

    with open("encrypted.txt", "r", encoding="UTF-8") as file3:
        text_secret = file3.read()

        for i in text_secret:
            if i.islower():
                up = True

            if i.upper() in alfavit:
                i = i.upper()
                place = alfavit.find(i)
                new_place = place - 3
                letter = alfavit[new_place]

            else:
                result += i

            if up:
                letter = letter.lower()
                up = False
                result += letter
                letter = ""

            else:
                result += letter
                letter = ""

    with open("decrypted.txt", "w", encoding="UTF-8") as file4:
        file4.write(result)
except Warning:
    print("Неизвестная ошибка!!!")
