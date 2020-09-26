#покупка телефона
print('Введіть суму грошей,яку ви маєте на покупку телефона:')
money=int(input())
telephon=6000
if money>=telephon:
    print("Мерщій за телефоном!")
else:
    a=telephon-money
    print("Не вистачає",a, "гривень. Відкладайте ще.")
