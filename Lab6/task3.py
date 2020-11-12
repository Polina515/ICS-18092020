class Successor(str):
    def replies_of_queue(self, s):
        for i, char in enumerate(s):
            if(i <= len(s)-2):
                if(char == s[i] and char == s[i+1] and char == s[i+2]):
                    return True
                return False

    def is_palindrom(self, raw):
        if(raw == ''):
            return True

        reversed_raw = raw[::-1]
	
        if(reversed_raw == raw):
            return True
        else:
            return False
	
my_str = Successor()
print('ЧИ МІСТИТЬ РЯДОК ПОВТОРИ ПОСЛІДОВНОСТЕЙ СИМВОЛІВ ДОВЖИНОЮ ВІД 3?')
s1 = input('ВВЕДІТЬ РЯДОК ДЛЯ АНАЛІЗУ: ')
print(my_str.replies_of_queue(s1))
print("\n")
print('ЧИ Є РЯДОК ПОЛІНДРОМОМ?')
s2 = input('ВВЕДІТЬ СТРОКУ ДЛЯ АНАЛІЗУ: ')
print(my_str.is_palindrom(s2))


	                
