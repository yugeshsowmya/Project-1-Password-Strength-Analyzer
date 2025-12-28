def leetspeak(word):
    substitutions = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1'],
        'o': ['0'],
        's': ['$', '5']
    }

    variations = set([word])

    for char, subs in substitutions.items():
        if char in word:
            for sub in subs:
                variations.add(word.replace(char, sub))

    return variations

def append_years(words, start=1990, end=2025):
    mutated = set()

    for word in words:
        for year in range(start, end + 1):
            mutated.add(f"{word}{year}")

    return mutated
