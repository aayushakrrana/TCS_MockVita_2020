'''Prime Fibonnaci
Problem Description
Given two numbers n1 and n2

1. Find prime numbers between n1 and n2, then

2. Make all possible unique combinations of numbers from the prime numbers list you found in step 1. 

3. From this new list, again find all prime numbers.

4. Find smallest (a) and largest (b) number from the 2nd generated list, also count of this list.

5. Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till the count (number of primes in the 2nd list).

6. Print the last number of a Fibonacci series as an output

Constraints
2 <= n1, n2 <= 100

n2 - n1 >= 35

Input Format
One line containing two space separated integers n1 and n2.

Output
Last number of a generated Fibonacci series.

Timeout
1


Test Case
Example 1

Input

2 40

Output

13158006689

Explanation

1st prime list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

Combination of all the primes = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]

2nd prime list=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317]

smallest (a) = 23

largest (b) = 3719

Therefore, the last number of a Fibonacci series i.e. 34th Fibonacci number in the series that has 23 and 3719 as the first 2 numbers is 13158006689

Example 2

Input

30 70

Output

2027041 

Explanation

1st prime list=[31, 37, 41, 43, 47, 53, 59, 61, 67]

2nd prime list generated form combination of 1st prime list = [3137, 5953, 5347, 6761, 3761, 4337, 6737, 6131, 3767, 4759, 4153, 3167, 4159, 6143]

smallest prime in 2nd list=3137
largest prime in 2nd list=6761

Therefore, the last number of a Fibonacci series i.e. 14th Fibonacci number in the series that has 3137 and 6761 as the first 2 numbers is 2027041
'''

def isprime(n):
  if n<=1:
    return False
  if n==2:
    return True
  if n>2 and n%2==0:
    return False
  for i in range(3,int(n**0.5)+1,2):
    if n%i==0:
      return False
  return True

def find_comb(list1):
  comb=[]

  for i in range(len(list1)):
    for j in range(len(list1)):
        if i==j:
            continue 
        else:
            comb.append(int(str(list1[i])+str(list1[j])))
  return comb

def fib1(n,a,b):
    fib=[0]*(n+1)
    fib[0]=a
    fib[1]=b
    fib[2]=a+b
    for i in range(3,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n-1]

a,b=map(int,input().split())
prime_list=[]
for i in range(a,b+1):
  if isprime(i):
    prime_list.append(i)
combination=set(find_comb(prime_list))
combination1=[i for i in combination if isprime(i)]

max1=max(combination1)
min1=min(combination1)
ans1=fib1(len(combination1),min1,max1)
print(ans1,end="")





'''
JAVA SOLUTION FULL WORKING


import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class PrimeFibo{
    static boolean[] genPrime(int n1, int n2, ArrayList<Integer> al){
        boolean prime[]=new boolean[n2+1];
        Arrays.fill(prime,true);
        prime[1]=false;
        for(int i=2;i<=n2;i++){
            if(prime[i]){
                for(int j=i*i;j<=n2;j=j+i){
                    prime[j]=false;
                }
            }
        }
        for(int i=n1;i<=n2;i++){
            if(prime[i]){
                al.add(i);
            }
        }
        return prime;
    }
    public static void main(String args[]){
        ArrayList<Integer> al=new ArrayList<Integer>();
        Scanner sc=new Scanner(System.in);
        String items[]=sc.nextLine().split(" ");

        genPrime(Integer.parseInt(items[0]),Integer.parseInt(items[1]),al);
        int min=Integer.parseInt(al.get(0)+""+al.get(1));
        int max=Integer.parseInt(al.get(al.size()-1)+""+al.get(al.size()-2));
        ArrayList<Integer> al2=new ArrayList<Integer>();
        boolean prime[]=genPrime(min,max,al2);
        al2=new ArrayList<>();
        long min2=Integer.MAX_VALUE;
        long max2=Integer.MIN_VALUE;
        HashSet<Integer> hs=new HashSet<Integer>();
        for(int i=0;i<al.size();i++){
            for(int j=0;j<al.size();j++){
                if(i!=j) {
                    int num = Integer.parseInt(al.get(i) + "" + al.get(j));
                    if (prime[num] && !hs.contains(num)) {
                        //System.out.println(num);
                        hs.add(num);
                        max2 = Math.max(max2, num);
                        min2 = Math.min(min2, num);
                    }
                }
            }
        }

        long a=min2;
        long b=max2;
        long c=0;

        for(int i=2;i<hs.size();i++){
            c=a+b;
            a=b;
            b=c;
        }
        System.out.println(c);



    }
}

'''