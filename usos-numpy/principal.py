import numpy as np

vector = [1, 2, 3, 4, 5]
vector1 = [1, 1, 2, 2, 3]

def verificar_pyton():
    multi = []
    resultado = []
    for v in vector:
        print(v, end=" ")

    print()

    for v in vector:
        multi = v * 2
        print(multi, end=", ")

    # Suma entre vectores
    for i in range(len(vector)):
        resultado.append(vector[i] + vector1[i])

    print("")
    print(resultado)



def verificar_numpy():
    v = np.array(vector)
    print(v)
    print(v * 2)

    suma = vector + vector1
    print(suma)

def main():
    print("=========== Solo Python ===========")
    verificar_pyton()
    print("\n\n=========== NumPy ===========")
    verificar_numpy()


if __name__ == '__main__':
    main()
