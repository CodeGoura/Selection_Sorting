'''Sorting list in python method1 :- Selection Sorting Method-2: Bubble sort '''
#Method:1
# it work as follow i am writing the step below:
# let L=[1,2,-1,0,-2]
'''
Note:one thing if L[0] i=that is right -2 is smaller then other then no change done other wise is swap the 
Step1:
L[0] index i,e 1 is compare with each element on list then the smallest value is on left side of position i,e l[0]
i,e :[-2,2,1,0,-1]
step2:2nd small nos as followes position:
[-2,-1,2,1,0]
step3:
[-2,-1,0,2,1]
step4:
[-2,-1,0,1,2] .ans 
we know the total step is according to the list length: 
'''
#lets start this with python:
#get the list value from user input :
l=eval(input('Please Enter the list:\n'))
#1st check the list have contain more then one value that calculated by len and if fun.
print(f'your enterd list is : {l}')
if len(l)>1:
    # used for loop for this process:
    for i in range(1,len(l)):# the range value are(1,2..."n-1")
        # used cond'n for checking each element of l we get 1st element in L[i]
        for j in range(0,len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print(f'after sorting the list is {l}')
