# This class is designed for one purpose, and one purpose only:
#  - To generate normally distributed random variables with
#    a mean of 0 and a standard deviation of 1.
#  - This is done using the Box-Meuller algorithm for generating
#    such random numbers:
#       1. Given two uniformly distributed random variables from the
#          interval (0, 1], call these 'u1' and 'u2'.
#            - Uniformly distributed means every point has the same
#              likelihood of being selected.
#          The random.random() function returns a random value that
#          takes values in [0, 1), so '1 - random.random()' will
#          return a random value in (0, 1].
#       2. Let c = \/-2 ln( u1 )
#          Then two independent normally distributed random
#          variables are
#                n1 = c cos( 2 pi u2 )
#                n2 = c sin( 2 pi u2 )
# The randn() function works as follows:
#   If the function is called twice:
#     1. On the first call, the two random values 'n1' and 'n2' are
#        calculated. One ('n2') is stored in a class variable
#        'second_random_variable', while the other ('n1') is returned.
#     2. On the second call, the second ('n1') is returned.
# This is done through the use of two class variables:
#     The class variable 'call_count' records how often this function
#     has been previously been called.
#     If 'call_count' is even, then the function has been called an
#     even number of times, and thus, there must have been a previous
#     call that produced two normally distributed random variables,
#     and thus, one must be stored in the class variable
#     'second_random_variable'. This is what is returned.
#     If 'call_count' is odd, then it is necessary to generate both
#     normally distributed random variables, storing one of them in
#     the class variable 'second_random_variable' and returning the
#     other.
# Note, in almost all mathematics libraries, the natural logarithm
# is implemented with a function called 'log', while the common
# logarithm or base-10 logarithm is implemented with a function called
# 'log10'.
class BoxMueller:
        call_count = 0;
        second_random_variable = 0.0;
        @classmethod
        def randn( cls ):
                cls.call_count += 1;
                # If this function has been called an even number of
                # times, then on the previous call, two random variables
                # were generated, so the one of those two stored in the
                # class varible 'second_random_variable' can be returned.
                if cls.call_count%2 == 0:
                        return cls.second_random_variable;
                # Need to ensure the number is in (0, 1], not [0, 1)
                u1 = 1.0 - random.random();
                u2 = 1.0 - random.random();
                c = math.sqrt( -2.0*math.log(u1) );
                # Store one of the two random variables,
                #    and return the other
                cls.second_random_variable = c*math.sin( 2*math.pi*u2 );
                return c*math.cos( 2*math.pi*u2 );
# Create a list holding 16 entries
# Assign to each of these 16 entries a normally distributed random variable
# You can access these 16 entries by using white_noise[0] through
# white_noise[15]
# You will have to repeatedly change this seed
# Print it out, so that the user can convince one's self that they are
# apparently normally distributed with mean '0' and a standard deviation
# of '1'
import math
import random
import cmath
import numpy
#Question 1
white_noise = [None] * 16
random.seed(420420)
for i in range( 0, 16 ):
        white_noise[i] = BoxMueller.randn();
print("white_noise", white_noise )
white_noise_squared = 0
for i in range(0, 16):
        white_noise_squared += white_noise[i]**2
print("2-norm_of_white_noise", math.sqrt(white_noise_squared))
mean_white_noise = 0
for i in range(0, 16):
        mean_white_noise += white_noise[i]/16
print("average of white noise", mean_white_noise)
#The 2-norm of the white noise will always be significantly larger than the average since you are squaring and adding together positive and negative values whereas the average is compiled of positive and negative values
#and will typically result in a decimal number

#Question 2
#In terms of COVID-19 testing, reporting the number of positive tests on a day to day basis rather than over an averaged ten-day period would produce misinformed and inaccurate representations of exactly how volatile and
#dangerous the virus truly is. The number of reported cases on an individual day could be affected by a variety of different unforeseeable variables such as traffic, day of the week, or recent large mass gatherings such
#as Halloween. Due to this, if news outlets reported the number of cases on a daily basis the public might interpret a day with relatively low cases reported as a good sign and that COVID-19 is starting to slow.
#Conversely, if on a single day the number of cases reported was high in comparison to previous days the public might panic and believe that the pandemic is worse than it truly is. When reporting cases on a day to day
#basis this variance in reported cases is much more likely and will have a greater change in the number of cases. Furthermore, when analyzing an average over the course of ten days trendlines can be observed and compared
#to previous ten-day averages rather than comparing cases on individual days. This would be a better indicator of whether or not the cases in a given area are increasing or decreasing.

#Question 3
v = [[1]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16, [None]*16]
for i in range(1, 9):
        for j in range(0,16):
               v[i][j] = math.cos(2*math.pi*(i)*(j+0.5)/16)
for i in range(9, 17):
        for j in range(0, 16):
                v[i][j] = math.sin(2*math.pi*(i-8)*(j+0.5)/16)
print("initial 17 sine and cosine vectors", v)
v.pop(7)
print("final 16 sine and cosine vectors without zero vector", v)
#When f is equal to 8 the cosine function is equal to 0, therefore, that vector contains practically no useful information and is considered useless

#Question 4
x = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 16):
        for j in range(0, 16):
                x[i] += ((v[i][j])**2)
y = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 16):
        y[i] = math.sqrt(x[i])
print("2-norm of final 16-dimensional sine and cosine vectors", y)
for i in range(0, 16):
        for j in range(0, 16):
                v[i][j] = v[i][j]/y[i]
print("normalized 16-dimenesional sine and cosine vectors", v)

#Question 5
Q5A = [[0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16, [0.0]*16,]
for i in range(0, 16):
        for j in range(i, 16):
                for k in range(0, 16):
                        Q5A[i][j] += v[i][k]*v[j][k]
print("Inner product of every possible pair combination of the 16-dimensional vectors", Q5A)
#Whenever one of the 16-dimensional vectors is multiplied onto itself it returns the 1 vector, all other cases return the 0 vector since all of the vectors are orthongonal to eachother
#All returned vectors after running this code produce a variety of extremely small entries to e-16 or e-17, therefore, they can be assumed to be close enough to 0 to be the 0 vector.

#Question 6
InnerProduct = [0.0]*16
for i in range(0, 16):
        for j in range(0, 16):
                        InnerProduct[i] += v[i][j]*white_noise[j]
print("Inner Product", InnerProduct)
#The coefficients would be closer in mean when applying vectors of same or similar magnitude such as the vectors above with magnitude 0.25.

#Question 7, f=1, A=20, phase shift=+0.9197057831 for Q7 vector, Coefficients
Q7B = [0.0]*16
Coefficient = [0.0]*16
for i in range(0, 16):
    Q7B[i] = 20*math.sin(2*math.pi*1*((i+0.5)/16)+0.9197057831)
for i in range(0, 16):
        for j in range(0, 16):
                Coefficient[i] += Q7B[j]*v[i][j]
print("Coefficient Vector", Coefficient)
print("2-norm of Coefficient Vector", numpy.linalg.norm(Coefficient))
#All coefficients are very close to zero which we can assume to practically be equal to zero. The one exception being when the inner products hold the same frequency of the vector just created. Furthermore, the 2-norm is
#dependant on magnitude and where the vector is multiplied by amplitude. Lastly, multiplying the 2-norm by sin(phi) to return a cos vector of the same frequency. This also works in reverse

#Question 8
#The returned coefficient Vector given from when f = float and not when f = int gives us values which don't represent exact values pertaining to our exact frequencies. This resulting code is less useful in determining
#and containing information regarding our original 16-dimensional vector whic leads to it being more difficult to know which coefficient to use in our calculations. Without knowing the exact coefficient to use in our
#calculations, determining out original 16-dimensional vector, frequency, and amplitude will become measurably more challenging. We could always use estimations and approximations but even that becomes increasingly harder
#as our floats approach midpoints of two integers

#Question 9
Q9V = [-1.90, -6.05, -2.48, 2.82, -.324, 3.99, 5.22, -2.90, -.599, -1.64, -3.76, -2.97, 3.39, 4.23, 3.26, 3.35]
NormalizedQ9 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
TwoNormQ9 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(0, 16):
    NormalizedQ9[i] += ((Q9V[i])**2)
for i in range(0, 16):
    TwoNormQ9[i] = math.sqrt(NormalizedQ9[i])
for i in range(0, 16):
    NormalizedQ9[i] = Q9V[i] / TwoNormQ9[i]
for i in range(0, 16):
    Q9V[i] = numpy.dot(Q9V, NormalizedQ9)
for i in range(1,8):
    print("Frequency", i, ":", Q9V[i], Q9V[i + 8])
AmplitudeFetus = math.sqrt(Q9V[2]**2 + Q9V[10]**2)
AmplitudeMother = math.sqrt(Q9V[5]**2 + Q9V[13]**2)
print("Amplitude of Fetus", AmplitudeFetus)
print("Amplitude of Mother", AmplitudeMother)
BPMFetus = 2 / 16 * 60
BPMMother = 5 / 16 * 60
print("BPM of Fetus", BPMFetus)
print("BPM of Mother", BPMMother)

#Question 10
Q10V = [None]*16
for i in range(0, 16):
    Q10V[i] = math.cos(2 * math.pi * 13 * ((i+0.5)/16) + 2)
z1 = [1] * 16
z2 = [None] * 16
z3 = [None] * 16
z4 = [None] * 16
z5 = [None] * 16
z6 = [None] * 16
z7 = [None] * 16
z8 = [None] * 16
z9 = [None] * 16
z10 = [None] * 16
z11 = [None] * 16
z12 = [None] * 16
z13 = [None] * 16
z14 = [None] * 16
z15 = [None] * 16
z16 = [None] * 16
z17 = [None] * 16
for i in range(0, 16):
    z2[i] = math.cos(2*math.pi*((i+0.5)/16))
for i in range(0, 16):
    z3[i] = math.cos(2*math.pi*2*((i+0.5)/16))
for i in range(0, 16):
    z4[i] = math.cos(2*math.pi*3*((i+0.5)/16))
for i in range(0, 16):
    z5[i] = math.cos(2*math.pi*4*((i+0.5)/16))
for i in range(0, 16):
    z6[i] = math.cos(2*math.pi*5*((i+0.5)/16))
for i in range(0, 16):
    z7[i] = math.cos(2*math.pi*6*((i+0.5)/16))
for i in range(0, 16):
    z8[i] = math.cos(2*math.pi*7*((i+0.5)/16))
for i in range(0, 16):
    z9[i] = math.cos(2*math.pi*8*((i+0.5)/16))
for i in range(0, 16):
    z10[i] = math.sin(2*math.pi*((i+0.5)/16))
for i in range(0, 16):
    z11[i] = math.sin(2*math.pi*2*((i+0.5)/16))
for i in range(0, 16):
    z12[i] = math.sin(2*math.pi*3*((i+0.5)/16))
for i in range(0, 16):
    z13[i] = math.sin(2*math.pi*4*((i+0.5)/16))
for i in range(0, 16):
    z14[i] = math.sin(2*math.pi*5*((i+0.5)/16))
for i in range(0, 16):
    z15[i] = math.sin(2*math.pi*6*((i+0.5)/16))
for i in range(0, 16):
    z16[i] = math.sin(2*math.pi*7*((i+0.5)/16))
for i in range(0, 16):
    z17[i] = math.sin(2*math.pi*8*((i+0.5)/16))
a1 = (numpy.linalg.norm(z1))
a2 = (numpy.linalg.norm(z2))
a3 = (numpy.linalg.norm(z3))
a4 = (numpy.linalg.norm(z4))
a5 = (numpy.linalg.norm(z5))
a6 = (numpy.linalg.norm(z6))
a7 = (numpy.linalg.norm(z7))
a8 = (numpy.linalg.norm(z8))
a10 = (numpy.linalg.norm(z10))
a11 = (numpy.linalg.norm(z11))
a12 = (numpy.linalg.norm(z12))
a13 = (numpy.linalg.norm(z13))
a14 = (numpy.linalg.norm(z14))
a15 = (numpy.linalg.norm(z15))
a16 = (numpy.linalg.norm(z16))
a17 = (numpy.linalg.norm(z17))
normalized1 = (z1/a1)
normalized2 = (z2/a2)
normalized3 = (z3/a3)
normalized4 = (z4/a4)
normalized5 = (z5/a5)
normalized6 = (z6/a6)
normalized7 = (z7/a7)
normalized8 = (z8/a8)
normalized10 = (z10/a10)
normalized11 = (z11/a11)
normalized12 = (z12/a12)
normalized13 = (z13/a13)
normalized14 = (z14/a14)
normalized15 = (z15/a15)
normalized16 = (z16/a16)
normalized17 = (z17/a17)
print(numpy.dot(Q10V, normalized1))
print(numpy.dot(Q10V, normalized2))
print(numpy.dot(Q10V, normalized3))
print(numpy.dot(Q10V, normalized4))
print(numpy.dot(Q10V, normalized5))
print(numpy.dot(Q10V, normalized6))
print(numpy.dot(Q10V, normalized7))
print(numpy.dot(Q10V, normalized8))
print(numpy.dot(Q10V, normalized10))
print(numpy.dot(Q10V, normalized11))
print(numpy.dot(Q10V, normalized12))
print(numpy.dot(Q10V, normalized13))
print(numpy.dot(Q10V, normalized14))
print(numpy.dot(Q10V, normalized15))
print(numpy.dot(Q10V, normalized16))
print(numpy.dot(Q10V, normalized17))
