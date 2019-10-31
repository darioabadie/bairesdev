# BairesDev Coding Challenge
 
## Descripción
La siguiente aplicación analiza un archivo con datos de profesionales obtenidos de *Linkedin* a fin de identificar los **100 potenciales clientes** con mayor probabilidad de comprar los servicios de la empresa **BairesDev**.

## Criterio de selección de individuos
* No se considerarán individuos que no tengan un **puesto definido**.
* Los individuos ocuparán preferentemente **puestos directivos** en sus respectivas empresas (Ej CEO, CTO, Director, Vice presidente, etc). Esto surgió de una investigación sobre el perfil de los clientes que han compartido su experiencia con BairesDev ([Fuente](https://www.bairesdev.com/clients/)).
* Debido a que el 95% de los desarrolladores se encuentran en Latinamérica, se considera conveniente que los individuos **vivan en un país latinoamericano**. De esta manera la comunicación será más efectiva, con todos los beneficios que esto implica tanto para BairesDev, los desarrolladores y los clientes.
* Se busca que los individuos pertenezcan a alguna **industria en la cual BairesDev tenga experiencia desarrollando soluciones**. ([Fuente](https://www.bairesdev.com/clients/)).
* Se valorarán el **número de conexiones** y el **número de recomendaciones** que tengan los individuos. 

## Uso de la aplicación
La aplicación toma como entrada el archivo *people.in* y genera un archivo de salida *people.out* el cual contiene el listado de *PersonId* de los **100 potenciales clientes**.

## Mejoras de la aplicación
* Se puede analizar una base de datos con los clientes actuales de BairesDev a fin de caracterizar sus perfiles en términos de **ocupación**, **país** e **industria**. En base a esto sería posible optimizar los parámetros de ponderación empleados en el algoritmo actual.
* Sería factible entrenar una **red neuronal** con la base de datos de clientes actuales de BairesDev a fin de desarrollar un algoritmo de **inteligencia artificial** que identifique potenciales clientes en función de las características del perfil.