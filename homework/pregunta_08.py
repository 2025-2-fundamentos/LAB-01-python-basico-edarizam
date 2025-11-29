"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

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
                letra = fila[0]
                num = int(fila[1])

                if num not in info:
                    info[num] = set()
                
                info[num].add(letra)
        
        for key, value in info.items():
            datos.append((key, sorted(list(value))))
        
    return sorted(datos, key = lambda x: x[0])
