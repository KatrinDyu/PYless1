#Найдите сумму цифр трехзначного числа.

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) |


n = int(input("vvedite 3znachnoe chislo  "))
sum = 0
while n > 0:
    k = n % 10
    sum = sum + k
    n = n // 10
print(sum)