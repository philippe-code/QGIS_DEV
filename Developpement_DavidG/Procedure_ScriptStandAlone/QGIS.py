#!/usr/bin/env python
# coding: utf-8


"""
Auteur:

Par David Gauthier

Division des systemes d'information et du pilotage
Direction des inventaires forestiers
Ministere des Forets, de la Faune et des Parcs
Telephone: (418)-627-8669 poste 4322
Sans frais: 1-877-936-7397 poste 4322
Telecopieur: (418-646-1955
Courriel: david.gauthier@mffp.gouv.qc.ca

"""
# Historique:
# 2020-03-20 -Création du script


from qgis.core import *
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsNativeAlgorithms


# Chemin ou QGIS est installer
QgsApplication.setPrefixPath(r"E:\OSGeo4W64\bin", True)

# Créer une reference à QgsApplication,
# Mettre le 2eme argument a faux pour desativer l'interface graphique de QGIS
qgs = QgsApplication([], False)

# initialiser QGIS
qgs.initQgis()

# Initialiser les outils qgis
Processing.initialize()

# Permet d'utiliser les algorithmes "natif" ecrit en c++
# https://gis.stackexchange.com/questions/279874/using-qgis3-processing-algorithms-from-standalone-pyqgis-scripts-outside-of-gui
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

# Écrire les algorithmes que l'on veut appeler.

input = 'E:/Temp/geotraitement_QGIS/sub.shp'
output = 'E:/Temp/geotraitement_QGIS/extent.shp'
param = {'INPUT':input,'ROUND_TO':0,'OUTPUT':output}

# permet de sortir l'extent d'une couche
processing.run("qgis:polygonfromlayerextent", param)


input = 'E:/Temp/geotraitement_QGIS/sub.shp'
output = 'E:/Temp/geotraitement_QGIS/sommet.shp'
param = {'INPUT':input,'OUTPUT':output}

# permet d'extraire les sommets d'une couche
processing.run("native:extractvertices", param)

# Fermer QGIS, vide la memoire....
qgs.exitQgis()