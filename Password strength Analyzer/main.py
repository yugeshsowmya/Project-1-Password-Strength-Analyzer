import argparse

from analyzer import basic_password_analysis, zxcvbn_analysis
parser = argparse.ArgumentParser(description="Password Strength Analyzer with Wordlist Generator")

parser.add_argument(
    "-p", "--password",
    help="Password to analyze",
    required=False
)
parser.add_argument("--name", help="User name for wordlist")
parser.add_argument("--pet", help="Pet name for wordlist")
parser.add_argument("--year", help="Significant year for wordlist")

parser.add_argument(
    "--export",
    action="store_true",
    help="Generate and export custom wordlist"
)


args = parser.parse_args()


if args.password:
    password = args.password
else:
    password = input("Enter a password to analyze: ")


basic = basic_password_analysis(password)
advanced = zxcvbn_analysis(password)

print("\nBasic Analysis:")
for key, value in basic.items():
    print(f"{key}: {value}")

print("\nAdvanced Strength Analysis (zxcvbn):")
print("Score (0-4):", advanced["score"])
print("Estimated Crack Time:", advanced["crack_time"])

if advanced["score"] <= 1:
    print("Strength: WEAK")
elif advanced["score"] == 2:
    print("Strength: MEDIUM")
else:
    print("Strength: STRONG")

if advanced["feedback"]["warning"]:
    print("Warning:", advanced["feedback"]["warning"])

if advanced["feedback"]["suggestions"]:
    print("Suggestions:")
    for suggestion in advanced["feedback"]["suggestions"]:
        print("-", suggestion)

from wordlist import collect_user_inputs, generate_base_wordlist, export_wordlist

"""print("\n--- Custom Wordlist Generator ---")
inputs = collect_user_inputs()
wordlist = generate_base_wordlist(inputs)
export_wordlist(wordlist)"""

if args.export:
    print("\n--- Custom Wordlist Generator ---")

    name = args.name if args.name else input("Enter your name (optional): ")
    pet = args.pet if args.pet else input("Enter your pet name (optional): ")
    year = args.year if args.year else input("Enter a significant year (optional): ")

    user_inputs = {
        "name": name,
        "pet": pet,
        "year": year
    }

    wordlist = generate_base_wordlist(user_inputs)

    print(f"Wordlist generated with {len(wordlist)} entries")

    from mutations import leetspeak, append_years

    mutated_words = set()
    for word in wordlist:
        mutated_words.update(leetspeak(word))

    mutated_words.update(append_years(mutated_words))
    wordlist.update(mutated_words)

    export_wordlist(wordlist)

    print(f"Final wordlist size after mutations: {len(wordlist)}")
