#####    СКЛАДАННЯ ВИПАДКОВИХ ФРАЗ З ТРЬОХ СПИСКІВ   ####
import random

firstlist = [" місяць","небо"," зорі"," сонце"," земля"]
secondList = ["троядда", "тюльпан", "фіалка", "хризантема", "квітка", "кактус"]
thirdList = ["море", "гори", "місто", "поле", "водоспад", "озеро"]

random.shuffle(firstlist)#перемешивает слова в списке
f = random.choice(firstlist)#возвращает одно случайное слово

random.shuffle(secondList)
s = random.choice(secondList)

random.shuffle(thirdList)
t = random.choice(thirdList)

print(f + " " + s + " " + t) 
