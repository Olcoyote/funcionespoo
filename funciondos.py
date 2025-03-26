import random

#realizr funcion probabilidad

def Probabilidad(num_lanzamientos,num_caras):
    
    #simular los lanzamientos de la moneda
    resultados=[random.choice([0,1])] for _ in range (num_lanzamientos):
    
    #calaular la probabilidad de obtener el numero de caras
        prob=resultados.count(1)/num_lanzamientos
        return prob
    
    #ejemplos de uso (declaracion de objetos)
    num_lanzamientos=10
    num_caras=6
    
    prob=Probabilidad(num_lanzamientos,num_caras)
    print(f"la probabilidad de obtener {num_caras} caras en {num_lanzamientos} es {prob:.4f}")