import random as rand
import time
from vpython import *

answers = ['It is certain.', 'Without a doubt.', 'Yes, definitely.', 'Very doubtful.', 'Outlook not so\n good.', 'Reply hazy, \ntry again.', 'Dont count on\n it.','My sources say\n no.', 'You may rely\n on it.', 'Better not tell\n you now.']

#background, the black 8 ball, the gray background for text
canvas(background=color.hsv_to_rgb(vector (0.5,0.4,0.8)))
eightball = sphere(radius=15, color=color.black, pos=vector(-5.4, 0, 0), shininess=0.3)
backgroundball = sphere(radius=4, color=vector(0.5, 0.5, 0.5), pos=vector(-3.9, 1, 15), shininess=0)

#text formatting
t = text(text="8", pos=vector(-3.4,0,20), align="center")
t.height = 2*t.height
t.length = 2.5*t.length

#name input
print('I am the Magic 8 Ball. What is your name?')
name = input()
time.sleep(0.3)
print('Hello ' + name + ".")

def main():
  time.sleep(1)
  #question input
  print('Ask me a question...')
  input()
  time.sleep(rand.randint(1, 3))

  #hide the background for text and hide the "8"
  backgroundball.visible = False
  t.visible = False

  #blue triangle background for new text
  T = triangle(v0=vertex(pos=vec(-10,-3,20),color=color.blue), v1=vertex( pos=vec(3,-3,20),color=color.blue),v2=vertex( pos=vec(-3.5, 5, 20), color=color.blue))

  #new text
  a = text(text=answers[rand.randint(0, len(answers)-1)], pos=vector(-3.5,-1,20), align="center")
  a.height = 0.7*a.height
  a.length = 0.8*a.length

  time.sleep(2)
  print('I hope this answered your question...')
  time.sleep(1.23)

main()