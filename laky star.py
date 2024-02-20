import pygame as p
import tkinter as t
import random





def player_boom(event):
    if event.keysym =='w':
        canvas.move(player,0,-20)
    if event.keysym =='a':
        canvas.move(player,-20,0)
    if event.keysym=='s':
        canvas.move(player,0,20)
    if event.keysym=='d':
        canvas.move(player,20,0)



def create_point():
   global point
   point_pos=(random.randint(1,400), random.randint(1, 400 ))
   point=canvas.create_oval(point_pos[0],point_pos[1],point_pos[0]+50,point_pos[1]+50 ,fill='#8FBC8F')

def restart_game():
    global canvas,player
    start_pos=(random.randint(1,400), random.randint(1, 400 ))
    point_pos=(random.randint( 1,  350),random.randint(1,   350))
    player =canvas.create_rectangle(start_pos[0],start_pos[1],start_pos[0]+50,start_pos[1]+50 ,fill='#00BFFF')
    restart_bt.config(state='disabled')
    create_point()
root =t.Tk()
root.title('my game ')
root.geometry('400x400')

label_score=t.Label(root , text='boomomomomomomo')
restart_bt =t.Button(root,text='satart',command=restart_game )
canvas=t.Canvas(root,width=400, height=400,bg='#B22222')

player=''
point=''
restart_bt.pack()
canvas.pack()
label_score.pack()
root.mainloop()
root.bind('<KeyPress>', player_boom)