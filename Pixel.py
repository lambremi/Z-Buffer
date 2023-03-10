N = 500     #Number of pixel
Size = 1000  #sizeWindows
n = Size/N
marge = 10


def draw_pixel(window, x, y, z, n,color="black"):
    x1 = x*n+marge
    y1 = Size-y*n+marge
    x2 = n*(x+1)+marge
    y2 = Size-n*(y+1)+marge
    if(color == "black"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#%02x%02x%02x" % (int(z), int(z), int(z)), outline="#%02x%02x%02x" % (int(z), int(z), int(z)))
    if(color == "red"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#%02x0000" % int(z), outline="#%02x0000" % int(z))
    if(color == "blue"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#0000%02x" % int(z), outline="#0000%02x" % int(z))
    if(color == "green"):
        window.create_rectangle(x1,y1 ,x2 ,y2 , fill="#00%02x00" % int(z), outline="#00%02x00" % int(z))
    x_center = (x1+x2)/2
    y_center = (y1+y2)/2
    #window.create_text(x_center, y_center, text=z, fill="white",font=("Helvetica", int(0.4*n)))