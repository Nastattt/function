# #1
# number = int(input())
# Flag = True
#
# for i in range(2, number // 2 + 1):
#     if number % i == 0:
#         Flag = False
#         break
#
# if Flag and number > 1:
#     print("Простое число")
# else:
#     print("Не подходит")
#
# #2
# array = list(map(int,input().split()))
# for j in range(len(array)-1):
#     for i in range(len(array)-1-j):
#         if array[i] > array[i+1]:
#             array[i],array[i + 1] = array[i + 1],array[i]
# print(array)

# #3
# array = list(map(int,input().split()))
# maxi = array[0]
# for i in array:
#     if i > maxi:
#         maxi = i
# print(maxi)





