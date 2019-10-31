
# Librerías
import pandas as pd 
import matplotlib.pyplot as plt



# Lectura del archivo people.in

data = []
with open ("people.in", "r") as myfile:
    data.append(myfile.read())

# Parseo de los datos
data = data[0].splitlines()
df = pd.DataFrame(data)
df[["PersonId", "Name", "LastName", "CurrentRole", "Country", "Industry", "NumberOfRecommendations",
"NumberOfConnections"]] = df[0].str.split("|",expand=True,)

df = df[["PersonId", "Name", "LastName", "CurrentRole", "Country", "Industry", "NumberOfRecommendations",
"NumberOfConnections"]]
    
# Visualizaciones

## Pais
#
#paises = df["Country"].value_counts()
#df_paises = pd.DataFrame(paises)
#df_paises["Pais"] = df_paises.index
#labels = df_paises["Pais"]
#values = df_paises["Country"]
#
#fig1, ax1 = plt.subplots()
#ax1.pie(values, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()
#
## Pisición
#
#pos = df["CurrentRole"].value_counts()
#df_pos = pd.DataFrame(pos)
#df_pos["Posición"] = df_pos.index
#labels = df_pos["Posición"]
#values = df_pos["CurrentRole"]
#
#fig1, ax1 = plt.subplots()
#ax1.pie(values, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()
#
#
## Industria
#
#industria = df["Industry"].value_counts()
#df_ind= pd.DataFrame(industria)
#df_ind["Industria"] = df_ind.index
#labels = df_ind["Industria"]
#values = df_ind["Industry"]
#
#fig1, ax1 = plt.subplots()
#ax1.pie(values, labels=labels, autopct='%1.1f%%',
#        shadow=True, startangle=90)
#ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#plt.show()


# Industrias

#Banking & Financial ServicesCapital MarketsComputer GamesConsumer GoodsDesignElectrical/ Electronic ManufacturingEnergy, Resources & UtilitiesEntertainment & SportsGovernment
#HealthcareHigh TechHuman ResourcesInformation Technology & ServicesInsuranceManufacturingMedia & Information ServicesPharmaceuticals and Biotech
#PublishingReal Estate ServicesRetail & Consumer ProductsStaffing and RecruitingTelecomTextilesTolling & AutomationTravel, Transportation & Hospitality

# Clientes

# Product manager,  VP of engineering, SVP, Managing Director, Program manager, CTO, Business development, Director of architecture, VP Technology Services, CEO, Founder

# Regla:
# Filtrar por paises latinoamericanos, industrias y clientes. Luego ordenar de mayor a menor por numero de recomendaciones.
# HAcer una correlación/dispersion entre numero de contactos y de recomendaciones.



# Paises

countries = ["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","French Guiana", "Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela","Belize","Costa Rica", "El Salvador", "Guatemala", "Honduras","Mexico","Nicaragua","Panama"]
industries = ["Banking","Business Services", "Financial Services","Capital Markets","Computer Games","Consumer Goods","Design","Electrical Manufacturing","Electronics", "Electronic Manufacturing","Energy", "Resources", "Utilities","Entertainment", "Sports","Government",
              "Healthcare","High Tech","Human Resources","Information Technology","Insurance","Manufacturing","Media & Information Services", "Pharmaceuticals", "Biotech",
              "Publishing", "Real Estate", "Retail", "Consumer Products","Staffing", "Recruiting", "Telecommunications", "Textiles", "Tolling", "Automation", "Travel", "Transportation", "Hospitality"]

roles = ["product manager",  "VP of engineering", "SVP", "managing director", "program manager", "CTO", "business development", "director of architecture", "VP technology services", "CEO", "founder","owner", "chief executive officer",
         "vice president","president","project manager","director", "supervisor"]

             

              


#df2 = df[]  

#df["Country"] &in& paises



industria = df["Industry"].value_counts()
reco = df["NumberOfRecommendations"].value_counts()
cone = df["NumberOfConnections"].value_counts()
pos = df["CurrentRole"].value_counts()






df2 = df[df["CurrentRole"] != ""]

df2["Score"] = df2["CurrentRole"] 
df2 = df2.reset_index()

for ind in range(0,len(df2["CurrentRole"])):
    F_country = 20 if df2["Country"][ind] in countries else 0
    flag = 0
    for role in roles:
        if df2["CurrentRole"][ind] in role:
            flag = 1    
    F_role = 20 if flag == 1 else 0
    F_indistry = 10 if df2["Industry"][ind] in industries else 0
    F_connections = int(df2["NumberOfConnections"][ind])/500 * 10
    F_recommendations = int(df2["NumberOfRecommendations"][ind])/500 * 100
    df2["Score"][ind] = F_country + F_role + F_indistry + F_connections + F_recommendations
    
df3 = df2.sort_values(by=["Score"], ascending=False)
df4 = df3[:100]
    

