# Lesson 27

def stringCleaner(text):
    result = ''
    for character in text:
        if character.isalpha():
            result += character.lower()
    return result

value = stringCleaner("hiii1 hell0o")
print(f"value is {value}")