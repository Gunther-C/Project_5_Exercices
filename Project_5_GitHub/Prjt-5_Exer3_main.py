words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = "aeiou"
vowels_list = []

for wrd in words:
    count = 0

    for unity in wrd:
        if unity in vowels:
            count += 1

    vowels_list.append((wrd, count,))

print(f"{vowels_list}")
