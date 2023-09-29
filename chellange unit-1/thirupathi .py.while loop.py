Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> # program to calcnate factorial
... >>> n=int(input("Enter a positive integer : "))
... Enter a positive integer : 8
... >>> if(n<0):
... ...     print("NO factorial for negative numbers")
... ... elif(n==0):
... ...     print("The factorial for 0 is 1")
... ... else:
... ...     f=1
... ...     i=1
... ...     while(i<=n):
... ...         f=f*i
... ...         i=i+1
