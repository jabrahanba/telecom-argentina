import pandas as pd
import re

# Corregir provincias:
def transf_provincias(provincia):
    provincia =  provincia.title()
    if provincia == 'Caba':
        return 'Ciudad De Buenos Aires'
    elif provincia == 'Capital Federal':
        return 'Ciudad De Buenos Aires'
    elif provincia == 'Cordoba':
        return 'Córdoba'
    elif provincia == 'Entre Rios':
        return 'Entre Ríos'
    elif provincia == 'Neuquen':
        return 'Neuquén'
    elif provincia == 'Rio Negro':
        return 'Río Negro'
    elif provincia == 'Tierra Del Fuego':
        return 'Tierra Del Fuego, Antártida E Islas Del Atlántico Sur'
    elif provincia == 'Tucuman':
        return 'Tucumán'
    else:
        return provincia
    
#Lista de localidades que no están en todos los dataset y no se pueden usar en el analisis.
localidades_borrar = [
    'Agustín Mosconi',
    'Bellocq',
    'Berutti',
    'colonia la plata',
    'Colonia La Plata',
    'Garré',
    'General Alvear',
    'Desvío Aguirre',
    'Noetinger',
    'Osvaldo Magnasco',
    'La Ciénaga Y Barrio San Rafael',
    'La Caleta',
    'la rotonda',
    'La Rotonda',
    'Manuel Alberti',
    'Ostende',
    'La Ciénaga Y Barrio San Rafael',
    'Pearson',
    'Playa Dorada',
    'San Enrique',
    'Valdés',
    'Valeria del Mar',
    'Valeria Del Mar',
    'Vivoratá',
    'General Capdevila',
    'Gobernador Costa',
    'Canteras Quilpo',
    'Guasapampa',
    'La Rancherita',
    'La Serranita',
    'Los Chañaritos',
    'Lozada',
    'Nicolás Bruzzone',
    'Rafael García',
    'San Ignacio (Loteo Vélez Crespo)',
    'San Joaquín',
    'Talaini',
    'Pedernal',
    'Pueblo Cazes',
    'La Almona',
    'Loteo Navea',
    'Rio Blanco',
    'Pichi Huinca',
    'Castro Barros',
    'Guanchín',
    'Jagüé',
    'Machigasta',
    'Suriyaco',
    'Tuyubil',
    'Blanco Encalada',
    'Villa Atuel Norte',
    'Bajo San Cayetano',
    'Barrio Chacra Monte',
    'Barrio El Petróleo',
    'Barrio Fátima',
    'Barrio Frontera',
    'Barrio Isla 10',
    'Barrio La Barda',
    'Barrio La Costa',
    'Barrio La Defensa',
    'Barrio La Ribera - Barrio APYCAR',
    'Barrio Luisillo',
    'Barrio Mar del Plata',
    'Barrio Mar Del Plata',
    'Barrio Moño Azul',
    'Barrio Mosconi',
    'Barrio Norte (municipio de Cipolletti)',
    'Barrio Norte (Municipio De Cipolletti)',
    'Barrio Pinar',
    'Barrio Porvenir',
    'Barrio Puente 83',
    'Barrio Santa Lucia',
    'Barrio Santa Rita',
    'Barrio Unión',
    'Ingeniero Otto Krause',
    'Paso Córdova',
    'Pichi Mahuida',
    'Puente Cero',
    'Villa Alberdi',
    'Villa del Parque',
    'Villa Del Parque',
    'Villa El Salvador',
    'Palo Negro'
]


# Corregir localidades:
def transf_localidades(localidad):
    localidad = re.sub(r'\s+', ' ', localidad) #eliminar los espacios dobles y triples
    localidad = localidad.title() #colocar todas como nombre propio
    if pd.isna(localidad) or localidad == '':  #llenar las vacias y localidades que no serán estudiadas con 'Otros'
        localidad = 'Otros'
    elif localidad in localidades_borrar:
        localidad = 'Otros'
    elif localidad == 'Ciudad Autónoma De Buenos Aires':
        localidad = 'Palermo' #En los dataset todas las localidades de CABA aparecen agrupadas, las reflejaré en Palermo, la localidad más grande en población
    #localidad = localidad.replace('\s+', ' ') 
    return localidad











