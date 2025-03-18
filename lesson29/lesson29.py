# Lesson 29

def consonantCount(text, vowel = False):
    counter = 0
    for character in text:
        character = character.lower()
        if character.isalpha() and character in {'a', 'e', 'i', 'o', 'u'}:
            counter += 1
    if not vowel:
        return counter
    else:
        counter = 0

        for character in text:
            character = character.lower()
            if character.isalpha() and character in {'a', 'e', 'i', 'o', 'u'}:
                counter += 1
        return counter

print(f"The number of consonants is {consonantCount('hiiii i like marshmallows')}")