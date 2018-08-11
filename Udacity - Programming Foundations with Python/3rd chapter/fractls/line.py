import turtle

def draw_triangle(T1):
     for i in range (0,2):
        T1.forward(200)
        T1.right(120)

def draw_Semi(M):
      M.forward(100)
      V = M.forward(100)
      draw_triangle(V)    
      M.right(90)
      M.forward(10)
      M.right(90)
      M.forward(100)
             
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red") 
    
    T = turtle.Turtle()
    T.color("yellow","blue")
    T.shape("turtle")
    T.speed(5)
    
    for i in range(0,36):
        draw_Semi(T)
        T.right(10)    
        
    #for i in range(0,36):
            
    T.right(90)
    T.forward(400)         
    window.exitonclick()

draw_art()

        