num = 0

def enterAppreciation():
    print( 'Please enter a rating from 1 to 5' )
    point = input()
    while(not point.isdecimal or int(point) <= 0 or int(point) > 5):
        print('Please enter a valid number.')
        point = input()   
    print( 'Enter your comment' )
    comment = input()
    post = f'point: {point} comment: {comment}'
    file_pc = open("data.txt", 'a')
    file_pc. write( f'{ post } \n')
    file_pc.close()
                 
def printAppreciations():
    print( 'results so far' )
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

while (num != 3):
    print( 'Select the process you want to perform' )
    print( '1: Enter evaluation points and comments' )
    print( '2: Check the results so far' )
    print( '3: Exit' )
    num = int(input())
    
    if num == 1:
        enterAppreciation()       
    elif num == 2:
        printAppreciations()
    elif num == 3:
        print( 'Terminate' )
        break # Syntax to end the iterating process       
    else:
        print( 'Enter 1 to 3' )
