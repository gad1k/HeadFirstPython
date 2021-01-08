def search4letters(phrase: str, letters: str = "aeiou") -> set:
    """Возвращает множество букв из "letters", найденных в указанной фразе"""
    return set(letters).intersection(set(phrase))


help(search4letters)
print(search4letters("Python", "ot"))
print(search4letters("Python"
                     ))
