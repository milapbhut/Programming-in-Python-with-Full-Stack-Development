str = (input("Enter a string: ")).lower()

vowels = 0
consonants = 0

for char in str:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")