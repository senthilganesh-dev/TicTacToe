from math import floor
a=[[f"{i}" for i in range(1,4)],[f"{i}" for i in range(4,7)],[f"{i}" for i in range(7,10)]]
scorex,scorey=0,0
play="x" 
def disp():
    print(f"ScoreX:{scorex}\tScoreY:{scorey}")
    for i in range(3):
        for j in range(3):
            print(a[i][j]+'|',end=" ")       


        print('')
        print('-'*9) if i!=2 else print()
   
def winlos():
    if a[0][0]==a[0][1]==a[0][2] or a[0][0]==a[1][0]==a[2][0] or a[0][2]==a[1][
        2]==a[2][2] or a[2][0]==a[2][1]==a[2][2] or a[0][0]==a[1][1]==a[2][2] or a[0][2]==a[1][1]==a[2][0]:
        print(f"{a[0][0]} is winner")
        disp()
        return False
                  
    return True
        
def player():
    if  all(i.isalpha() for j in a for i in j):
            print("Match is drawn")
            exit(0)
    global scorex,scorey,play
    print(f"Player{play}: ",end=" ")
    ch=int(input())
    
    row,col=(ch-1)//3,(ch-1)%3
    check= lambda ch: False if a[row][col]==['x','o'] else True
    a[row][col]=play if check(ch) else print("Invlaid choice")
    scorex = scorex + 1 if check(ch) and play == 'x' else scorex
    scorey = scorey + 1 if check(ch) and play != 'x' else scorey

   
    play="x" if play!="x" else "o"

    



if __name__=="__main__":
    while winlos():
        disp()
        player()
        
        
