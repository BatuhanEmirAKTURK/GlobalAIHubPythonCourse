"""Even numbers between zero and 'n' (including 'n')"""

print("""
----------------------------------------------

   Press the 'x' key to find an even number

        Press the 'q' key to log out

----------------------------------------------
""")

while True:

    selection = input("\nSelect the action you want to do:")

    if selection == "x" or selection == "X":

        zero_list = []
        
        n = int(input ("\nPlease,enter a single digit integer number:"))#User can write any positive number
        for i in range(n+1): #I do not process the zero value
            if i % 2 == 0: #Numbers that can be divided by two without a remainder
                zero_list.append(i)
        print(zero_list)

    elif selection == "q" or selection == "Q":
        print("\nSigning Out")
        break
