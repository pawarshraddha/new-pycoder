Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Numpy assignment
>>> # Q1
>>> a = np.array([12,13,12,15,16,18,12,10,11,19])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = np.array([12,13,12,15,16,18,12,10,11,19])
NameError: name 'np' is not defined
>>> import numpy as np
>>> a = np.array([12,13,12,15,16,18,12,10,11,19])
>>> a=a.reshape(5,2)
>>> print(a)
[[12 13]
 [12 15]
 [16 18]
 [12 10]
 [11 19]]
>>> 
>>> 
>>> # Q2
>>> arr = np.array([1,3,4,8,9,3,1,7,4,8,9,10])
>>> np.unique(arr)
array([ 1,  3,  4,  7,  8,  9, 10])
>>> 
>>> 
>>> # Q3
>>> P = np.tile( np.array([[0,1],[1,0]]),(5,5))
>>> P[1:-1,1:-1] = 7
>>> print(P)
[[0 1 0 1 0 1 0 1 0 1]
 [1 7 7 7 7 7 7 7 7 0]
 [0 7 7 7 7 7 7 7 7 1]
 [1 7 7 7 7 7 7 7 7 0]
 [0 7 7 7 7 7 7 7 7 1]
 [1 7 7 7 7 7 7 7 7 0]
 [0 7 7 7 7 7 7 7 7 1]
 [1 7 7 7 7 7 7 7 7 0]
 [0 7 7 7 7 7 7 7 7 1]
 [1 0 1 0 1 0 1 0 1 0]]
>>> 
>>> 
>>> #Q4
>>> a1 = np.array([[4,3],[3,6]])
>>> a2 = np.array([[2,1],[4,5]])
>>> s = np.dot(a1, a2)
>>> print(s)
[[20 19]
 [30 33]]
>>> 