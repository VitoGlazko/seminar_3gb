#Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

n = int(input("Сколько элементов должно быть в списке?: "))
num1 = 1
num2 = 1
print(num1, num2, end=' ')
for i in range(n-2):
        num1, num2 = num2, num1 + num2
        print(num2, end=' ') 
