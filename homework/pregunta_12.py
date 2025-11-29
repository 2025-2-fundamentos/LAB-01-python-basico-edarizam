"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

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
                letra = fila[0]

                for diccionario in diccionarios:
                    diccionario = diccionario.split(':')

                    valor = int(diccionario[1])

                    if letra not in info:
                        info[letra] = 0
                
                    info[letra] += valor
        
        return info
