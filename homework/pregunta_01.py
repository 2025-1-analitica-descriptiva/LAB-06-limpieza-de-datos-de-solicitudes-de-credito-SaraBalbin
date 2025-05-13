"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd
    import os

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
    df = df.dropna() 

    df['sexo'] = df.sexo.str.lower()

    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()

    df['idea_negocio'] = df.idea_negocio.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.replace('_', ' ')
    df['idea_negocio'] = df.idea_negocio.str.replace('-', ' ')
    df['idea_negocio'] = df.idea_negocio.str.strip()

    df['barrio'] = df.barrio.str.lower()
    df['barrio'] = df.barrio.str.replace('_', ' ')
    df['barrio'] = df.barrio.str.replace('-', ' ')

    def fechas(fecha):
        partes = fecha.split('/')
        p1, p2, p3 = partes[0], partes[1], partes[2]
        if len(p1) == 4:
            date = '/'.join(reversed(partes))
        else:
            date = '/'.join(partes)
        return date

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(fechas)

    df['monto_del_credito'] = df.monto_del_credito.str.replace(' ', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace('$', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito.astype(float)

    df['línea_credito'] = df.línea_credito.str.lower()
    df['línea_credito'] = df.línea_credito.str.replace('_', ' ')
    df['línea_credito'] = df.línea_credito.str.replace('-', ' ')

    df = df.drop_duplicates(
            subset=["sexo", "tipo_de_emprendimiento", 'idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 
            'fecha_de_beneficio','monto_del_credito', 'línea_credito'],
        )
    
    print(os.path.exists("files/output"))
    if not os.path.exists("files/output"):
        os.makedirs("files/output")

    df.to_csv(
        "files/output/solicitudes_de_credito.csv",
        sep=";",
        header=True,
        index=False,    
    )

pregunta_01()
