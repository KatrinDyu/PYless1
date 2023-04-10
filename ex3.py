# сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

#*Пример:*

#385916 -> yes
#123456 -> no
k = int(input("vvedite 6znachnoe tchislo  "))
k1 = k // 1000
print(k1)
k2 = k % 1000
print(k2)
summk1 = 0
while k1 > 0:
    cifra = k1 % 10
    summk1 = summk1 + cifra
    k1 = k1 // 10
print(summk1)
summk2 = 0
while k2 > 0:
    cifk2 = k2 % 10
    summk2 = summk2 + cifk2
    k2 = k2 // 10
print(summk2)
if summk1 == summk2:
    print("yes")
else:
    print("no")