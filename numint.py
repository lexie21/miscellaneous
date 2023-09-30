#raw
def trapezoidal_integration(a,b):
    area = 0
    base = (b-a)/100
    while a<b:
        x = a
        area += 1/2*base*(x**2+(x+base)**2)
        a += base 
    return area

print(trapezoidal_integration(1,2))

#builtin
import scipy.integrate as integrate

result = integrate.quad(lambda x: x**2,1,2)
print(result)

