# x,y,n = map(int,input().split())
# for i in range(1,n+1):
#     if(i%x==0 and i%y==0):
#         print("FizzBuzz")
#     elif(i%x==0):
#         print("Fizz")
#     elif(i%y==0):
#         print("Buzz")
#     else:
#         print(i)



n = input("Enter : ")

len_n = len(n)
sum = 0
i = 0
result = ""

while len_n != 0:
    sum += (int(n[len_n - 1]) * 2 ** i)
    i += 1

    if i > 2:
        i = 0
        result = str(sum % 8) + result  # Append the remainder to the left
        sum = 0

    len_n -= 1

# Check if there's a remaining sum after the loop
if sum != 0:
    result = str(sum) + result

print(result)
