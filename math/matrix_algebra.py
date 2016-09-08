# Matrix Algebra
import numpy

A = numpy.matrix(((1,2,3),(2,7,4)))
B = numpy.matrix(((1,-1),(0,1)))
C = numpy.matrix(((5,-1),(9,1),(6,0)))
D = numpy.matrix(((3,-2,-1),(1,2,3)))
u = numpy.array([6,2,-3,5])
v = numpy.array([3,5,-1,4])
w = numpy.matrix(((1,),(8,),(0,),(5,)))

# Dimensions:

#1.1 2x3
print"A dimensions\n", A.shape
#1.2 2x2
print "B dimensions\n", B.shape
#1.3 3x2
print "C dimensions\n", C.shape
#1.4 2x3
print "D dimensions\n", D.shape
#1.5 1x4
print "u dimensions\n", u.shape
#1.6 4x1
print "w dimensions\n", w.shape


# 2.1 [9,7,-4,9]
print "u + v\n", u + v

#2.2 [3,-3,-2,1]
print "u - v\n", u - v

#2.3 [36,12,-18,30]
print "6*u\n",  6*u

#2.4 51 
print "u dot v\n", numpy.dot(u,v)
#2.5 ~8.6023
print "||u||\n", numpy.linalg.norm(u)


#3.1 not defined
print "A + C is undefined\n"
#3.2
#[[-4, -7, -3],[3, 6, 4]]
print "A - Ctran\n" , A - C.transpose()

#3.3[[14, 3, 3],[2, 7, 9]]
print "Ctran + 3D\n", C.transpose() + 3*D

#3.4 [[-1, -5, -1], [2, 7, 4]]
print "BA\n", B*A

#3.5 Undefined
print "BAtran is undefined\n"



