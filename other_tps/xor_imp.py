w = [1, 1]
w2 = [1, -1]
b = [1, 1]
b2 = 1

vecteur1 = [0, 1]
vecteur2 = [0, 1]
o = [0, 0, 0, 0]
xor_result = [0, 0, 0, 0]

def z_function(b, x1, x2, associated_b, w):
    return x1*w[0] + x2*w[1] + b*associated_b

def aggregation_function(z_func):
    return 0 if z_func < 0 else 1

def xor_function(x1, x2):
    return 0 if x1 == x2 else 1

for i in vecteur1:
    for j in vecteur2:
        print('#####')
        print('x1=', vecteur1[i])
        print('x2=', vecteur2[j])
        n1 = aggregation_function(z_function(-0.5, vecteur1[i], vecteur2[j], b[0], w))
        print('n1=', n1)
        n2 = aggregation_function(z_function(-1.5, vecteur1[i], vecteur2[j], b[1], w))
        print('n2=', n2)
        o[i*2+j] = aggregation_function(z_function(-0.5, n1, n2, b2, w2))
        print('o=', o[i*2+j])

for i in vecteur1:
    for j in vecteur2:
        print('#####')
        print('x1=', vecteur1[i])
        print('x2=', vecteur2[j])
        xor_result[i*2+j] = xor_function(vecteur1[i], vecteur2[j])
        print('xor=', xor_result[i*2+j])
        
print('#####')
print('xor result: ', xor_result)
print('o result: ', o)
