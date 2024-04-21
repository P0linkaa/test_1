def sort_length(strings):
    # Сортируем строки по их длине в порядке возрастания
    sorted_strings = sorted(strings, key=len)
    
    # Сортируем строки по их длине в порядке убывания
    sorted_strings_descending = sorted(strings, key=len, reverse=True)
    
    return sorted_strings, sorted_strings_descending

strings = ["apple", "banana", "orange", "kiwi", "pineapple"]
ascending_order, descending_order = sort_length(strings)

print("Список строк по возрастанию длины:", ascending_order)
print("Список строк по убыванию длины:", descending_order)
