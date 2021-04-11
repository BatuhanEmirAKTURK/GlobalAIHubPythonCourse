"""Even numbers between zero and 'n' (including 'n')"""

while True:

    zero_list = []

    n = int(input ("\nPlease,enter a single digit integer number:"))#User can write any positive number

    for i in range(n+1): #I do not process the zero value
        if i % 2 == 0: #Numbers that can be divided by two without a remainder
            zero_list.append(i)
    print(zero_list)



    
