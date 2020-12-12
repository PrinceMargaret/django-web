'''import random
import keyword
while 1:
    a=eval((input("guess no.")))
    if a==random.randint(1,6):
        print(f"congratulation : you guess {a}")
    else:
        print("Ohho try Again")
    if keyword.iskeyword("q")==a:
        break'''
#import googlemaps
#for i in range(5):
    #print(i)
'''for j in range(5,1,-2):
    print(j)'''

####--PrinceMargaret--####
'''l=None
if l!=0 :  # Why this codition is true ??????
     print("None is  not equal to 0")

else:
    print("None is equal to 0")
   
if l:     # Why this condition is False ??????
     print("None is  not equal to 0")

else:
    print("None is equal to 0")

       ####   Output  ####
       None is  not equal to 0
       None is equal to 0
            # Why #'''


# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity W 


'''def knapSack(W, wt, val, n): 

	# Base Case 
	if n == 0 or W == 0: 
		return 0

	# If weight of the nth item is 
	# more than Knapsack of capacity W, 
	# then this item cannot be included 
	# in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
			knapSack(W, wt, val, n-1)) 

# end of function knapSack 


#Driver Code 
val = [11,21,31,33] 
wt = [2,11,22,15] 
W = 40
n = len(val) 
print (knapSack(W, wt, val, n) )'''

# This code is contributed by Nikhil Kumar Singh 

import nmap 

# take the range of ports to 
# be scanned 
begin = 75
end = 80

# assign the target ip to be scanned to 
# a variable 
target = '127.0.0.1/20'

# instantiate a PortScanner object 
scanner = nmap.PortScanner() 

res=scanner.scan(target,"53")
print(res)
