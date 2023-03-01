from graphics import *
def main():
    win=GraphWin("CSE 341", 400, 400)
    win.setBackground(color_rgb(200, 100, 50))

#circle
    pt1=Point(250, 250)  #X,Y_Value
    cir=Circle(pt1, 50)  #50_is_Radius_value
    cir.setFill(color_rgb(255, 255, 255))
    cir.setOutline(color_rgb(100,200,145))
    cir.setWidth(5)
    cir.draw(win)

    
#line
    ln=Line(Point(250,250), Point(250,300))
    ln.setWidth(5)
    ln.draw(win)
    

#Traingle
    tri=Polygon(Point(150,150), Point(200,200), Point(150,200))
    tri.setFill(color_rgb(100,100,100))
    tri.setWidth(5)
    tri.draw(win)



    win.getMouse()
    win.close()

    
    


main()
