'''
Television Sets
Problem Description
Dr. Vishnu is opening a new world class hospital in a small town designed to be the first preference of the patients in the city. Hospital has N rooms of two types - with TV and without TV, with daily rates of R1 and R2 respectively. 

However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead it follows a pattern. The number of patients on any given day of the year is given by the following formula – 

(6-M)^2 + |D-15| where

M is the number of month (1 for jan, 2 for feb ...12 for dec) and

D is the date (1,2...31).

All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and the values of N, R1 and R2 you need to identify the number of TVs the hospital should buy so that it meets the revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year. 

Constraints
Hospital opens on 1st Jan in an ordinary year

5 <= Number of rooms <= 100

500 <= Room Rates <= 5000

0 <= Target revenue < 90000000

Input Format
First line provides an integer N that denotes the number of rooms in the hospital

Second line provides two space-delimited integers that denote the rates of rooms with TV (R1) and without TV (R2) respectively

Third line provides the revenue target

Output
Minimum number of TVs the hospital needs to buy to meet its revenue target. If it cannot achieve its target, print the total number of rooms in the hospital.

Timeout
1


Test Case
Example 1

Input

20

1500 1000

7000000

Output

14 

Explanation

Using the formula, number of patients on 1st Jan will be 39, on 2nd Jan will be 38 and so on. Considering there are only twenty rooms and rates of both type of rooms are 1500 and 1000 respectively, we will need 14 TV sets to get revenue of 7119500. With 13 TV sets Total revenue will be less than 7000000

Example 2

Input

10

1000 1500

10000000

Output

10

Explanation

In the above example, the target will not be achieved, even by equipping all the rooms with TV. Hence, the answer is 10 i.e. total number of rooms in the hospital.
'''


N=int(input())
r1,r2=map(int,input().split())
Target=int(input())
l1,l2=[],[]
cost,final=0,0
l=[31,28,31,30,31,30,31,31,30,31,30,31]
for j in range(len(l)):
    for k in range(1,l[j]+1):
        l1.append((6-(j+1))**2+abs(k-15))
    l2.append(l1)
    l1=[]
for i in range(N+1):
    for j in l2:
        for k in j:
            if(k>=N):
                t=N-i
                cost=cost+(i*r1+t*r2)
            else:
                h=N-i
                t=k-h
                if(t<=0):
                    cost=cost+(k*r2)
                else:
                    cost=cost+(t*r1+h*r2)
        final=final+cost
        cost=0
    if(final>=Target):
        print(i)
        break
    else:
        final=0
else:
    print(N)