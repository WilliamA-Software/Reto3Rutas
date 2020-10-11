# -*- coding: utf-8 -*-
"""
Created on Spyder
@author: William Andres Otalora T
"""
#diccionarioA
distancias = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245, ('H', 'F'): 241,
('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254, ('A', 'E'): 179, ('A', 'F'): 41,
('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56, ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269,
('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80, ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180,
('D', 'H'): 30, ('D', 'A'): 40, ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109,
('E', 'H'): 33, ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55, ('F', 'F'): 0}

ruta_inicial = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']

def ruteo(distancias: dict, ruta_inicial: list)->dict:
    
    #validar mi diccionario, que no posea datos negativos
    validarDiccionario = validarDistancias(distancias)      #ir a la funcion validarDiccionario
    if(validarDiccionario == True):
        
        #copiar la ruta_inicial para luego comparar
        copia_ruta_inicial = ruta_inicial.copy()
        
        #declarar la bandera
        bandera = False
        
        #calculamos la distancia inicial que se establece
        calculoDistanciaRutaInicial = calcularDistancia(ruta_inicial, distancias)
        
        #INGRESO DE LOS CICLOS PARA CREAR NUEVAS RUTAS
        for i in range(1,len(ruta_inicial)-1):
            a = ruta_inicial[i]
            
            for j in range(i+1, len(ruta_inicial)-1):
                b = ruta_inicial[j]
                #crear el arco de los nuevos recorridos
                arco = (a,b)

                # llamar a la funcion para hacer los cambios de posicion a nuevas y retornar una nueva lista
                nueva_lista = cambioNuevaRuta(arco,copia_ruta_inicial)
                
                #calculo de la distancia que tiene la nueva_lista
                valor_nueva_lista = calcularDistancia(nueva_lista,distancias)                
                
                # CALCULAR 
                #condicional para comparar la nueva lista con la lista inicial
                if (valor_nueva_lista < calculoDistanciaRutaInicial):
                    
                    mejorRuta = nueva_lista.copy()
                    
                    calculoDistanciaRutaInicial = valor_nueva_lista
                    mejorDistancia = calculoDistanciaRutaInicial
                    #mejor ruta y mejor distancia van a ser nuestros valores mejores tomados
                    
                    bandera = True

            
            if((bandera == True)):
                i = 0
                bandera = False
                ruta_inicial = mejorRuta.copy()
                
                
            elif((bandera == False)):
                trayecto = {}
                
                #Guardar el resultado en un string
                #crear nuestro caracter separador (guion)
                separador = "-"
                #añadir la lista con las rutas separadas por guion
                mejorRuta = separador.join(mejorRuta)
                
                trayecto.update({"ruta" : mejorRuta})
                trayecto.update({"distancia" : mejorDistancia})  
                
                return trayecto
    else:
        return "Por favor revisar los datos de entrada."


#FUNCION PARA VALIDAR SI LAS DISTANCIAS INGRESADAS CUMPLEN CON EL ENUNCIADO
def validarDistancias(distancias):
    #Por defecto decimos que nuestro diccionario cumple perfectamente, es decir True
    valor_check = True
    
    #Recorrer nuestro diccionario
    for letra1Ruta, letra2Ruta in distancias:
        arco = (letra1Ruta,letra2Ruta)
        
        #verificar con if
        #si es negativo reporte como False
        #si es cero y sus valores son diferentes, reporte como False
        #sino significa que todo esta bien y marcha en orden así que su valor es el True inicial establecido
        if(distancias[arco] < 0):
            valor_check = False
        elif((distancias[arco] == 0) and (letra1Ruta != letra2Ruta)):
            valor_check = False
        elif((distancias[arco] != 0) and (letra1Ruta == letra2Ruta)):
            valor_check = False
    return valor_check 
        
#FUNCION QUE CALCULA LA DISTANCIA DE UNA RUTA INICIAL DADA
def calcularDistancia(ruta_inicial,distancias):
    
    sumaRutaInicial = 0

    #Recorrer cada uno de los arcos de la ruta inicial e ir sumando las distancias de cada uno
    #para así tener la la suma de las distancias de esa ruta inicial
    for i in range (len(ruta_inicial) - 1):
        arco = (ruta_inicial[i],ruta_inicial[i+1])
        #print(arco)
        sumaRutaInicial = sumaRutaInicial + distancias[arco]
    #print("la suma total es: " + str(sumaRutaInicial))
    
    return sumaRutaInicial
    
#FUNCION DE CAMBIO DE RUTAS DONDE CAMBIA LA POSICION
def cambioNuevaRuta(arco, copia_ruta_inicial):
    nuevaRuta = copia_ruta_inicial.copy()
    
    a = arco[0]
    b = arco[1]
    
    posicion_one = nuevaRuta.index(a)
    posicion_two = nuevaRuta.index(b)
    
    temp1 = nuevaRuta[posicion_one]
    temp2 = nuevaRuta[posicion_two]
    
    nuevaRuta[posicion_one] = temp2
    nuevaRuta[posicion_two] = temp1
    
    return nuevaRuta

print(ruteo(distancias, ruta_inicial))