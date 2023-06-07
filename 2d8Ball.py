import random
import time

answers = ['It is certain.', 'Without a doubt.', 'Yes, definitely.', 'Very doubtful.', 'Outlook not so good.', 'Reply hazy, try again.', 'Dont count on it.','My sources say no.', 'You may rely on it.', 'Better not tell you now.']

print('      /------------\ ')
time.sleep(1.23)
print('     /              \ ')
time.sleep(1.23)
print('    /       ___      \ ')
time.sleep(1.23)
print('   /       / _ \      \ ')
time.sleep(1.23)
print('  |       | (_) |      | ')
time.sleep(1.23)
print('  |        > _ <       |')
time.sleep(1.23)
print('  \       | (_) |      /')
time.sleep(1.23)
print('   \       \___/      /')
time.sleep(1.23)
print('    \                /   ')
time.sleep(1.23)
print('     \              /   ')
time.sleep(1.23)
print('      \------------/')
time.sleep(1.23)
print('\n\n\nI am the Magic 8 Ball. What is your name?')
name = input()
time.sleep(0.3)
print('Hello ' + name + ".")

def main():
  time.sleep(1)
  print('Ask me a question...')
  input()
  time.sleep(random.randint(1, 3))
  print(answers[random.randint(0, len(answers)-1)])
  time.sleep(2)
  print('I hope this answered your question...')
  time.sleep(1.23)
  replay()

def replay():
  print('Do you have another question(y/n)?')
  reply = input()
  if reply == 'y':
    main()
  elif reply == 'n':
    exit()
  else:
    print("Please retry.")
    replay()

main()
