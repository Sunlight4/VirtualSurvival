from Tkinter import *
from math import sqrt

def convert(x,y,z,centerx,centery):
    newx = centerx-x
    newy = int(sqrt((centery-z)**2+y**2)+0.5)
    return (newx, newy)

def sortfaces(faces):
    tmp = []
    for face in faces:
        z = 0
        for coord in face[0]:
            z+=coord[2]
        z = z/len(face[0])

        tmp.append([z,face])

    new = []

    tmp.sort(key=lambda x: x[0])

    tmp.reverse()
def render(model,pos,cam,canvas):
    for face in model:
        coords = []
        for coord in face[0]:
            coord[0] += pos[0]
            coord[1] += pos[1]
            coord[2] += pos[2]
            coords.append(convert(coord[0],coord[1],coord[2],cam[0],cam[1]))
            coord[0] -= pos[0]
            coord[1] -= pos[1]
            coord[2] -= pos[2]
        new = ""
        for i in coords:
            for j in i:
                new+=str(j)
                new+=','
        exec "canvas.create_polygon("+new+"fill=face[1])"
        print "canvas.create_polygon("+new+"fill=face[1])"
