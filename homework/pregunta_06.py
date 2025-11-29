"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    # 1. Define el nombre del archivo y el delimitador
    archivo_csv = 'files/input/data.csv'
    DELIMITADOR = '\t' # Asumimos la coma como separador

    # Lista para almacenar todos los datos procesados
    datos = []

    # Abre el archivo para lectura ('r')
    with open(archivo_csv, mode='r') as archivo:
        
        # 2. Iterar sobre el objeto 'archivo' (que itera línea por línea)
        info = {}
        for linea in archivo:
            # Elimina espacios en blanco y saltos de línea al principio/final
            linea_limpia = linea.strip() 
            
            if linea_limpia: # Asegúrate de que la línea no esté vacía
                
                # 3. Divide la línea en una lista de valores usando el delimitador
                # La fila será una lista de cadenas, igual que con csv.reader
                fila = linea_limpia.split(DELIMITADOR)
                
                # 4. Procesar o almacenar la fila
                diccionarios = fila[4].split(',')

                for diccionario in diccionarios:
                    diccionario = diccionario.split(':')

                    letra = diccionario[0]
                    valor = int(diccionario[1])

                    if letra not in info:
                        info[letra] = [float('INF'),0]
                
                    currentMinValue = info[letra][0]
                    currentMaxValue = info[letra][1]

                    if valor < currentMinValue:
                        currentMinValue = valor

                    if valor > currentMaxValue:
                        currentMaxValue = valor 
                    
                    info[letra] = [currentMinValue, currentMaxValue]

        for key, value in info.items():
            minimo = value[0]
            maximo = value[1]

            datos.append((key, minimo, maximo))
        
    return sorted(datos, key = lambda x: x[0])
