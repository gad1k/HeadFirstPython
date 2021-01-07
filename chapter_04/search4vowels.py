def search4vowels(word):
    """Выводит гласные, найденные в указанном слове"""
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


search4vowels("Hello")
