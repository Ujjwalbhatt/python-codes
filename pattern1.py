        # * * * * * * 
        #  * * * * * 
        #   * * * * 
        #    * * * 
        #     * * 
        #      * 
i=0
k=0
j=0
rows=int(input("Enter the number of the rows: "))
for i in range(1,rows+1, 1):
    for k in range(1, i, 1):
        print(" ",end="")
    
    for j in range(rows+1, i,-1):
        if (i == rows or j == 1 or j == 2*i - 1):
            print("* ", end="")
    print("")