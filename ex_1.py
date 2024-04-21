def unique_elements(input_list):
    # Создаем список для уникальных элементов
    unique_list = list(set(input_list))
    
    # Возвращаем список уникальных элементов
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5, 9, 15, 9]
print(unique_elements(input_list))
