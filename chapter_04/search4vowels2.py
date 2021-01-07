def search4vowels(word):
    """Возвращает булево значение в зависимости от присутствия любых гласных"""
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    return bool(found)


print(search4vowels("Hello"))
