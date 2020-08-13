#Instancia de QgsProject y guardamos en variable project
project = QgsProject.instance()

#Caracteristicas del proyecto
project.absoluteFilePath()
project.absolutePath()
project.baseName()
project.count()
project.crs()
project.distanceUnits()
project.areaUnits()

#Cargar un proyecto
project.read('C:\\ISM_PyQGIS\\01_project.qgs')

#Guardar un proyecto
project.write('C:\\ISM_PyQGIS\\01_project_v2.qgs')

#Llamar a la capa activa y gardarlo en una variable llamada lyr 
lyr  = iface.activeLayer()

#Obtener propiedades de la capa
lyr.name()
lyr.extent()
lyr.crs()
lyr.dataProvider().storageType()
lyr.dataProvider().dataSourceUri()
lyr.dataProvider().metadata()
lyr.dataProvider().wkbType()

#Obtener todas las entidades con un iterador y guardarlo en una variable llamada features
features = lyr.getFeatures()

#Convertit en lista la variable features
features = list(features)

#¿Cuantas entidades tenemos?
len(features)

#Obtener el primer elemento de la lista y guardarlo en una variable llamada feature
feature = features[0]

#Obtener el nombre de la entidad guardada en la variable feature accedendio a su atributo en el campo XXXX
feature ["sitename"]

#Obtener la geometria de las entidad guardada en la variable feature
feature.geometry()

#Listado de todss las entidades por el campo XXXX
[feature ["sitename"] for feature in features]

#Listado de la geometry de todos las entidades
[feature.geometry() for feature in features]

#Suma del area de todas las entidades
sum([feature ["area"] for feature in features])

#Estadíaticos de las entidades
mean([feature ["area"] for feature in features])
stdev ([feature ["area"] for feature in features])
max ([feature ["area"] for feature in features])
min ([feature ["area"] for feature in features])
median ([feature ["area"] for feature in features])

#Suma del area de todas las entidades filtrado a traves de dos métodos
sum([feature ["area"] for feature in iface.activeLayer().getFeatures('"NAME_1"=\'Castilla y León\'')])#Ejemplo bueno
sum([feature ["area"] for feature in features if feature["NAME_1"]== "Castilla y León"])#Ejemplo malo

#Crear capa de tipo punto y WGS84 llamada layer en memoria virtual
layer = QgsVectorLayer("Point?crs=ESPG:4326","capa","memory")

#Creamos objeto de tipo campo
field = QgsField("id", QVariant.String)

#Insertamos campo en capa layer
layer.dataProvider().addAttributes([field])

#Acualizamos campos
layer.updateFields()

feature = QgsFeature()
feature.setFields(layer.fields())
feature.setAttribute("id","1")
feature ["id"]

point = QgsPointXY(-3.70256, 40.4165)
geom = QgsGeometry.fromPointXY(point)
feature.setGeometry(geom)
layer.dataProvider().addFeatures([feature])

