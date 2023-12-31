def fibonacci(n):
    if n <= 0:
      #  return "Invalid input. Please enter a positive integer."
      raise ValueError
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

#num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
#for i in range(1, num_terms + 1):
   # print(fibonacci(i), end=" ")
    #print(fibonacci(5))
