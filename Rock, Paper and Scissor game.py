print('Game starts')
print('To end the game enter exit')
import random 
p=['rock','paper','scissor']
pc,pu=0,0
while True:
    i=input('Rock, Paper or Scissor ')
    com=random.choice(p)
    i.lower()
    if i=='exit':
        if pc>pu:
            print('Your total points :',pu,'My total points:',pc,'\nYOU LOSE')
        elif pu>pc:
            print('Your total points :',pu,'My total points:',pc,'\nYOU WIN')
        else:
            print('Your total points :',pu,'My total points:',pc,'\nNO RESULT')
        print('exit')
        break
    elif i=='rock':
        if com=='rock':
            ans='Rock can\'t beat Rock'
        elif com=='paper':
            ans='Paper beats Rock'
            pc+=1
        elif com=='scissor':
            ans='Rock beats Scissor'
            pu+=1
        print('Your total points :',pu,'My total points:',pc,'\n',ans)
    elif i=='paper':
        if com=='rock':
            ans='Paper beats rock'
            pu+=1
        elif com=='paper':
            ans='Paper can\'t beat Paper'
        elif com=='scissor':
            ans='Scissor beats Paper'
            pc+=1
        print('Your total points :',pu,'My total points:',pc,'\n',ans)
    elif i=='scissor':
        if com=='rock':
            ans='Rock beats Scissor'
            pc+=1
        elif com=='paper':
            ans='Scissor beats Paper'
            pu+=1
        elif com=='scissor':
            ans='Scissor can\'t beat Scissor'
        print('Your total points :',pu,'My total points:',pc,'\n',ans)
    else:
        print('Check your spelling')
	
