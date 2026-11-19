sentence = input("Enter a sentence: ")

print("========================================")
print("DOCUMENT ANALYSIS REPORT")
print("========================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.lower() in "aeiou":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

total_letters = vowels + consonants
if total_letters > 0:
    vowel_pct = (vowels / total_letters) * 100
else:
    vowel_pct = 0.0

print("")
print("--- Character Breakdown ---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special}")

print("")
print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_pct:.1f}%")

print("")
print("========================================")
print("Analysis Complete!")
print("========================================")
