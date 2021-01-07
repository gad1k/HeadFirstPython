def search4vowels(word):
    """Возвращает булево значение в зависимости от присутствия любых гласных"""
    vowels = set("aeiou")
    return vowels.intersection(set(word))


print(search4vowels("Hello"))
