from pickle import TRUE
from sqlite3 import Cursor
from turtle import color
from xml.dom.minidom import Entity
from erosion import *


app = Ursina( )

camera.orthographic =TRUE
camera.fov =4
camera.position =(1,1)
Test.defult_resolution *= 2

player =Entity(name='O', color= color . azure)
cursor + Tooltip(player.name, color=player.color, orgin)