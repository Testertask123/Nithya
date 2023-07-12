# prime number 1, 3, 5, 7, 11, 13
# 10 /2  ==0 its not a prime number
# 7/2 ===!0  its a prime number

num = int(input("enter the number-->"))  # 7/2   7/3  7/4 7/5  7/6 7/7
                                     # 7/i   7/i  7/i 7/i  7/i 7/i
for i in range(2,num):
    if num % i ==0:
        print("its not prime number")
        break
else:
    print("its a prime number")



