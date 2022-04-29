def hermit_interpolate(input):  #input is list of tuples [(x1,y1),(x2,y2),...,(xn,yn)] xi are Chebyshev nodes
    n = len(input)
points = numpy.zeros(shape=(2 * n + 1, 2 * n + 1))
X, Y = zip(*input)
X = list(X)
Y = list(Y)

for i in range(0, 2 * n, 2):
    points[i][0] = X[i / 2]
    points[i + 1][0] = X[i / 2]
    points[i][1] = Y[i / 2]
    points[i + 1][1] = Y[i / 2]

for i in range(2, 2 * n + 1):
    for j in range(1 + (i - 2), 2 * n):
        if i == 2 and j % 2 == 1:
            points[j][i] = calculate_f_p_x(X[j / 2]);

        else:
            points[j][i] = (points[j][i - 1] - points[j - 1][i - 1]) / (
                points[j][0] - points[(j - 1) - (i - 2)][0])

def result_polynomial(xpoint):  #here is function to calculate value for given x
    val = 0
    for i in range(0, 2 * n):
        factor = 1.
        j = 0
        while j < i:
            factor *= (xpoint - X[j / 2])
            if j + 1 != i:
                factor *= (xpoint - X[j / 2])
                j += 1
            j += 1
        val += factor * points[i][i + 1]
    return val
return result_polynomia 
