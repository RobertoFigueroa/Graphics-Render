from render import Render

from obj import Obj

my_bmp_file = Render()
my_bmp_file.glInit()
my_bmp_file.glCreateWindow(1000,1000)
my_bmp_file.glClearColor(0,0,1)

my_bmp_file.loadModel('./models/pato.obj', (500,500 ), (10,10) )


my_bmp_file.glFinish('lab3.bmp')
