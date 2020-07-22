n = 10
total_numbers = n
sum=0
while (n >= 0):
    sum += n
    n-=1
print ("sum using while loop ", sum)

num = int(input("Enter a number: "))




num = 7




if num > 1:

   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")



