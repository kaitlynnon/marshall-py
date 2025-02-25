# message = input("Enter a cipher: ")



# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# original = ""
# i = 0
# while i < len(message):
#     current = message[i]
#     if current != " ":
#         newLocation = alphabet.index(current)
#         newLocation = newLocation - shift
#         newLocation = newLocation % 26
#         original += alphabet[newLocation]
#     else:
#         original += " "
#     i += 1

i = 0
original = ""
while i < len(message):
    if message[i] != " ":
        newLocation = (ord(message[i]) - 65 - shift) % 26
        newLocation += 65
        original += chr(newLocation)
    else:
        original += " "
    i += 1
print(original)
