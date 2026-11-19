print("========================================")
print("          TEXT PROCESSING TOOL")
print("========================================")
sentence = input("Enter a sentence: ")

print("")
print("--- Processing Results ---")
pos = int(input("Enter position for indexing: "))
char = sentence[pos]
print(f"Character at position {pos}  : '{char}'")

start = int(input("Enter start index for slicing : "))
end = int(input("Enter end index for slicing   : "))
sliced = sentence[start:end]
print(f"Sliced string [{start}:{end}]           : '{sliced}'")

upper_text = sentence.upper()
lower_text = sentence.lower()
print(f"Uppercase                     : {upper_text}")
print(f"Lowercase                     : {lower_text}")

old_word = input("Enter word to replace         : ")
new_word = input("Enter replacement word        : ")
replaced_text = sentence.replace(old_word, new_word)
length = len(sentence)

print(f"After replace                 : {replaced_text}")
print(f"Length of sentence            : {length}")

print("")
print("========================================")
print("Analysis Complete!")
print("========================================")
