"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    # 1. Define el nombre del archivo y el delimitador
    archivo_csv = 'files/input/data.csv'
    DELIMITADOR = '\t' # Asumimos la coma como separador

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

                    if letra not in info:
                        info[letra] = 1
                    else:
                        info[letra] += 1

        return info
