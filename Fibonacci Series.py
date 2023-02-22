n=int(input("Enter the number of terms in the series :"))
a=0
b=1
i=0

if n <= 0:
  print("Invalid input")
elif  n == 1:
    print(" The Fibonacci sequence of", n,"terms is :")
    print(a)
else:
    print(" The Fibonacci sequence of", n,"terms is :")
    while i < n:
        print(a)
        c = a + b
        a = b
        b = c
        i += 1

 
