from World import *

world = World()
canvas = world.ca(width=500, height=500, background='white')

bbox = [[-150,-110], [150, 110]]

canvas.rectangle(bbox, outline='purple', width=5, fill='green')

canvas.oval(bbox, outline='purple', width=5, fill='yellow')

canvas.circle([0,0], 100, outline='purple', width=5, fill='orange')

canvas.line(bbox, fill='purple', width=5)

photo = PhotoImage(file='allen.ppm')
image = canvas.image([0,0], image=photo)

bbox = image.bbox()

canvas.rectangle(bbox, outline='purple', width=5, fill=None)

wait_for_user()
