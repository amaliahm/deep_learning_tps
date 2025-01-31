w = [1, 1]
b = [1, 1]
b2 = 1

def z_function(b, x1, x2, associated_b):
    return x1*w[0] + x2*w[1] + b*associated_b

def aggregation_function(z_func):
    return 0 if z_func < 0 else 1

vecteur1 = [0, 1]
vecteur2 = [0, 1]
o = [0, 0, 0, 0]

print(len(vecteur1))

for i in vecteur1:
    for j in vecteur2:
        n1 = aggregation_function(z_func(-0.5, vecteur1[i], vecteur2[j], b[0]))
        n2 = aggregation_function(z_func(-1.5, vecteur1[i], vecteur2[j], b[1]))
        o[i+j] = aggregation_function(z_func())