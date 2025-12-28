def collect_user_inputs():
    name = input("Enter your name (optional): ").strip().lower()
    pet = input("Enter your pet name (optional): ").strip().lower()
    year = input("Enter a significant year (optional): ").strip()

    inputs = []
    if name:
        inputs.append(name)
    if pet:
        inputs.append(pet)
    if year:
        inputs.append(year)

    return inputs

def generate_base_wordlist(inputs):
    wordlist = set()

    values = [v for v in inputs.values() if v]

    for i in range(len(values)):
        for j in range(len(values)):
            if i != j:
                wordlist.add(values[i] + values[j])

    return wordlist

def export_wordlist(wordlist, filename="wordlist.txt"):
    with open(filename, "w") as file:
        for word in sorted(wordlist):
            file.write(word + "\n")

