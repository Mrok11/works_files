with open("combined.txt", "+w", encoding="utf-8") as file:
    with open("file1.txt", "r", encoding="utf-8") as file1:
        text = file1.read()
    file.write(f"=== содержимое file1.txt ===\n[{text}]\n\n\n")
    with open("file2.txt", "r", encoding="utf-8") as file2:
        text = file2.read()
    file.write(f"=== содержимое file2.txt ===\n[{text}]\n\n\n")
    with open("file3.txt", "r", encoding="utf-8") as file3:
        text = file3.read()
    file.write(f"=== Содержимое file3.txt ===\n[{text}]\n\n\n")
