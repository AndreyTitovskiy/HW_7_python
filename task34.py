# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def count_vowels(word):
    vowels = "aeiouаеёиоуыэюя"
    return sum(1 for char in word if char in vowels)

def check_rhythm(poem):
    lines = poem.split()
    syllables_count = None
    
    for line in lines:
        words = line.split("-")
        line_syllables = sum(count_vowels(word) for word in words)
        
        if syllables_count is None:
            syllables_count = line_syllables
        elif line_syllables != syllables_count:
            return "Пам парам"
    
    return "Парам пам-пам"

poem_input = 'пара-ра-рам рам-пам-папам па-ра-па-да'
result = check_rhythm(poem_input)
print(result)
