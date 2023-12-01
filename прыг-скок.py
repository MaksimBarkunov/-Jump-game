from tkinter import*
import time
import random
class Ball:
    def __init__(self,canvas,color,racet):
        self.cht = 0
        self.run = True
        self.racet = racet
        self.x = 1
        self.y = -3
        self.canvas = canvas
        self.id = canvas.create_oval(0,0,15,15,fill = color)
        canvas.move(self.id,250,250)
    def drow(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <=0:
            self.y = 3
        elif self.hit(pos):
            self.y = -3
            self.cht += 1
        elif pos[3] >=500:
            self.run = False
        elif pos[0] <=0:
            self.x = 3
        elif pos[2] >=500:
            self.x = -3
    def hit(self,pos):
        racet_pos = self.canvas.coords(self.racet.platform)
        if pos[0] >= racet_pos[0] and pos[2] <= racet_pos[2]:
            if pos[3] <= racet_pos[3] and pos[3] >= racet_pos[1]:
                return True
        return False


class Racet:
    def __init__(self,canvas,color_p):
        canvas.bind_all("<Left>",self.left)
        canvas.bind_all("<Right>",self.right)
        self.x = 0
        self.canvas = canvas
        self.platform = canvas.create_rectangle(0,0,100,10,fill = color_p)
        canvas.move(self.platform,200,450)
    def drow(self):
        self.canvas.move(self.platform,self.x,0)
        pos = self.canvas.coords(self.platform)
        if pos[0] <= 0:
            self.x = 2
        elif pos[2] >= 500:
           self.x = -1

    def left(self,e):
        self.x = -3
    def right(self,e):
        self.x = 3


root = Tk()
root.title("прыг-скок")
root.resizable(0,0)
root.wm_attributes("-topmost",1)
canvas = Canvas(root,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
root.update()
racet = Racet(canvas,"blue")
ball = Ball(canvas,"red",racet)

r = canvas.create_text(420,30,text=f"СЧЕТ:{ball.cht}",font=("Arial",20))

while ball.run:
    canvas.itemconfig(r,text =f"СЧЁТ:{ball.cht}")
    root.update()
    root.update_idletasks()
    time.sleep(0.01)
    ball.drow()
    racet.drow()
canvas.create_rectangle(100,200,400,300,fill = "red")
canvas.create_text(250,250,text = "Вы ПРОИГРАЛИ",font=("Arial",25),fill="white")
root.update()
time.sleep(3)

