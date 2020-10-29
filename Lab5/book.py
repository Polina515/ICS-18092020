book = "Pollyanna by Eleanor H. Porter.txt"
def count_total_amout_of_chars_with_spaces():
    file = open("Pollyanna by Eleanor H. Porter.txt", 'r')
    data = file.read()
    total_amount = len(data)

    file.close()

    return total_amount

def count_total_amout_of_chars_without_spaces():


    num_chars = 0


    with open("Pollyanna by Eleanor H. Porter.txt", 'r') as f:
        for line in f:
            for letter in line:
                for i in letter:
                    if(i != ' ' and i != '\n'):
                        num_chars += 1


    return num_chars
def total_amout_of_words_in_file():
    num_words = 0
    words_set = set()  # кількість різних слів
    # кількість неповторюваних слів
    one_time_words = set()
    words_array = []


    with open("Pollyanna by Eleanor H. Porter.txt", 'r') as f:
        for line in f:


            words = line.split()
            num_words += len(words)


            for word in words:
                words_set.add(word)
                words_array.append(word)


    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            one_time_words.add(words_array[i])


    print(f'Загальна кількість різних слів у тексті: {len(words_set)}')
    print(f'Кількість слів,що не повторюються: {len(one_time_words)}')


    return num_words


print(f'Кількість символів з пробілами: {count_total_amout_of_chars_with_spaces()}')
print(f'Кількість слів без пробілів: {count_total_amout_of_chars_without_spaces()}')
print(f'Кількість слів: {total_amout_of_words_in_file()}')
