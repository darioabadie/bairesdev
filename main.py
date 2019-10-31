
# Librerías
import pandas as pd 

# Lectura del archivo people.in
data = []
with open ("people.in", "r") as myfile:
    data.append(myfile.read())

# Parseo de los datos y ordenamiento en un dataframe
data = data[0].splitlines()
df = pd.DataFrame(data)
df[["PersonId", "Name", "LastName", "CurrentRole", "Country", "Industry", "NumberOfRecommendations",
"NumberOfConnections"]] = df[0].str.split("|",expand=True,)

df = df[["PersonId", "Name", "LastName", "CurrentRole", "Country", "Industry", "NumberOfRecommendations",
"NumberOfConnections"]]
    
# Ponderación de las características de los individuos
role_weight = 30 # Peso asignado al puesto
country_weigth = 20 # Peso asignado al país
industry_weight = 15 # Peso asignado a la industria
connections_factor = 1/50 # Factor asignado al número de conexiones
recommendations_factor = 1/5 # Peso asignado número de recomendaciones

# Listas utilizadas para filtrar y ponderar datos

# Lista de paises latinoamericanos
countries = ["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","French Guiana", "Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela","Belize","Costa Rica", "El Salvador", "Guatemala", "Honduras","Mexico","Nicaragua","Panama"]

# Lista de industrias en las que BairesDev ha desarrollado soluciones
industries = ["Banking","Business Services", "Financial Services","Capital Markets","Computer Games","Consumer Goods","Design","Electrical Manufacturing","Electronics", "Electronic Manufacturing","Energy", "Resources", "Utilities","Entertainment", "Sports","Government",
              "Healthcare","High Tech","Human Resources","Information Technology","Insurance","Manufacturing","Media & Information Services", "Pharmaceuticals", "Biotech",
              "Publishing", "Real Estate", "Retail", "Consumer Products","Staffing", "Recruiting", "Telecommunications", "Textiles", "Tolling", "Automation", "Travel", "Transportation", "Hospitality"]

# Puestos que ocupan los clientes de BairesDev
roles = ["product manager",  "VP of engineering", "SVP", "managing director", "program manager", "CTO", "business development", "director of architecture", "VP technology services", "CEO", "founder","owner", "chief executive officer",
         "vice president","president","project manager","director", "supervisor"]


# Filtrado de datos
df2 = df[df["CurrentRole"] != ""]    # Se eliminan los individuos que no tienen una posición definida          

# Asignación de puntaje a cada individuo
df2["Score"] = df2["CurrentRole"]  # Creación de la característica Score (Puntaje)
df2 = df2.reset_index()

for ind in range(0,len(df2["CurrentRole"])): # Proceso de ponderación
    
    F_country = country_weigth if df2["Country"][ind] in countries else 0 # Ponderación por país
    flag_role = 0
    
    for role in roles: # Ponderación por puesto
        if df2["CurrentRole"][ind] in role:
            flag_role = 1  
    F_role = role_weight if flag_role == 1  else 0
    
    F_indistry = industry_weight if df2["Industry"][ind] in industries else 0 # Ponderación por industria
   
    F_connections = int(df2["NumberOfConnections"][ind])* connections_factor # Ponderación por número de conexiones
    
    F_recommendations = int(df2["NumberOfRecommendations"][ind])* recommendations_factor # Ponderación por número de recomendaciones
    
    df2["Score"][ind] = F_country + F_role + F_indistry + F_connections + F_recommendations # Puntaje final
 
# Selección de los 100 individuos con mayor puntaje (Posibles clientes)    
df3 = df2.sort_values(by=["Score"], ascending=False)
df4 = df3[:100]

# Almacenamiento de la lista de IDs de los clientes en un archivo
with open('people.out', 'w') as f:
    for item in df4["PersonId"]:
        f.write("%s\n" % item)

