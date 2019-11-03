# BairesDev Coding Challenge
 
## Descripción
La siguiente aplicación analiza un archivo con datos de profesionales obtenidos de *Linkedin* a fin de identificar los **100 potenciales clientes** con mayor probabilidad de comprar los servicios de la empresa **BairesDev**.

## Uso de la aplicación
Para hacer uso de la aplicación se debe ejcutar el archivo *bairesdev_clientes.exe*. La aplicación toma como entrada el archivo *people.in* y genera un archivo de salida *people.out* el cual contiene el listado de los **100 potenciales clientes** identificados por el parámetro *PersonId*. 


## Criterio de selección de la aplicación
A continuación se describen los criterios que utiliza la apliación para seleccionar los individuos que son considerados clientes potenciales de BairesDev.

* No se considerarán individuos que no tengan un **puesto definido**.
* Los individuos ocuparán preferentemente **puestos directivos** en sus respectivas empresas (Ej CEO, CTO, Director, Vice presidente, etc). Esto surgió de una investigación sobre el perfil de los clientes que han compartido su experiencia con BairesDev ([Fuente](https://www.bairesdev.com/clients/)).
* Debido a que el 95% de los desarrolladores se encuentran en Latinoamérica, se considera conveniente que los individuos **vivan en un país latinoamericano**. De esta manera la comunicación con los clientes será más efectiva, con todos los beneficios que esto implica tanto ellos como para BairesDev y sus desarrolladores.
* Se busca que los individuos pertenezcan a alguna **industria** en la cual BairesDev tenga experiencia **desarrollando soluciones**. ([Fuente](https://www.bairesdev.com/clients/)).
* Se valorarán el **número de conexiones** y el **número de recomendaciones** que tengan los individuos. 

## Principio de funcionamiento
Los siguientes pasos describen el funcionamiento de la aplicación:

* Cargar el contenido del archivo *People.in* en un dataframe.
* Eliminar los perfiles que no tienen un puesto definido.
* Crear la característica *Score* que se utiliza para cuantificar la posbilidad que tiene cada perfil de convertirse en cliente de BairesDev. Todos los perfiles inicialmente tienen *Score* = 0.
* Si el perfil tiene ubicación en Sudamérica añadir 30 unidades a su *Score*.
* Si el perfil cuenta con un cargo directivo en alguna compañia añadir  20 unidades a su *Score*.
* Si el perfil pertenece a alguna de las industrias en las cuales BairesDev tiene experiencia desarrollando soluciones añadir 15 unidades a su *Score*.
* Multiplicar el número de contactos que tiene el perfil por 1/50 y sumar dicho resultado a su *Score*.
* Multiplicar el número de recomendaciones que tiene el perfil por 1/5 y sumar dicho resultado a su *Score*.
* Ordenar la base de datos con los perfiles de mayor a menor *Score*.
* Seleccionar los 100 perfiles con mayor *Score*.
* Almacenar el resultado anterior en un archivo *People.out*.

## Mejoras de la aplicación
* Se puede analizar una base de datos con los clientes actuales de BairesDev a fin de caracterizar sus perfiles y así optimizar los parámetros de ponderación empleados en el algoritmo de selección actual.
* Sería factible desarrollar un algoritmo de **inteligencia artificial** utilizando la base de datos de clientes actuales de BairesDev. La arquitectura propuesta es un *Neural Network Classifier*, el cual tomará como dato de entrada un perfil de LinkedIn y como salida determinará si el mismo es un potencial cliente o no. Los pasos a seguir para implementar esta solución son los siguientes:
	* Identificar las características para analizar en cada perfil (*Feature selection*). Ej: Ubicación, industria, posición, número de contactos, número de recomendaciones, etc. 
	* Complementar la base de datos con perfiles de LinkedIn de personas que no son clientes de BairesDev (*Data augmentation*).
	* Etiquetar aquellos perfiles de personas que son clientes a fin de diferenciarlos en la base de datos de aquellas personas que no lo son (*Data labeling*).
	* Dividir la base de datos en dos porciones: una dedicada para entrenar la red neuronal (*training set*) y otra para evaluar la precisión de la misma (*testing set*).
	* Entrenar la red neuronal con el *traning set* empleando un algoritmo de aprendizaje supervisado (*Supervised learning*). Ej. Regresión lineal, *random forest* y *support vector machines*.
	* Evaluar la precisión de la red neuronal empleando el *testing set*.
	* Si la precisión obtenida es satisfactoria proceder a emplear el algoritmo con nuevos datos. Caso contrario entrenar la red con otros algoritmos de aprendizaje supervisado hasta obtener una precisión aceptable.