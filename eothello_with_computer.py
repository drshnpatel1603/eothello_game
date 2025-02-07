user = int(input("Enter the box size: "))
dict_computer = {}
count_computer = 0

# Create a 2D list (list of lists)
box = [[' ' for _ in range(user)] for _ in range(user)]
# Set initial positions
box[int(user / 2) - 1][int(user / 2) - 1] = 'W'
box[int(user / 2) - 1][int(user / 2)] = 'B'
box[int(user / 2)][int(user / 2) - 1] = 'B'
box[int(user / 2)][int(user / 2)] = 'W'

# Print the board nicely
for row in box:
    print(' '.join(row))

# Change Color only for user
def up(row,col,name):
    reverse_row = row
    flag = False
    row = row - 1
    if row < user and row >= 0:
        while row > 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
            elif box[row][col] == name:
                flag = True
                row += 1
            if flag:
                while reverse_row > row:
                    box[row][col] = name
                    row += 1
                break
        
def down(row,col,name):
    reverse_row = row
    flag = False
    row = row + 1
    if row < user and row >= 0:
        while row < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
            elif box[row][col] == name:
                flag = True
                row -= 1
            if flag:
                while reverse_row < row:
                    box[row][col] = name
                    row -= 1
                break
        
def right(row,col,name):
    reverse_col = col
    flag = False
    col = col + 1
    if col < user and col >= 0:
        while col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
            if flag:
                while reverse_col < col:
                    box[row][col] = name
                    col -= 1
                break
        
def left(row,col,name):
    reverse_col = col
    flag = False
    col = col - 1
    if col < user and col >= 0:
        while col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
            if flag:
                while reverse_col > col:
                    box[row][col] = name
                    col += 1
                break
        
def up_right(row,col,name):
    reverse_row = row
    flag = False
    reverse_col = col
    row -= 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row >= 0 and col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
                row += 1
            if flag:
                while reverse_row > row and reverse_col < col:
                    box[row][col] = name
                    col -= 1
                    row += 1
                break
        
def down_right(row,col,name):
    reverse_row = row
    flag = False
    reverse_col = col
    row += 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row < user and col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
                row -= 1
            if flag:
                while reverse_row < row and reverse_col < col:
                    box[row][col] = name
                    col -= 1
                    row -= 1
                break
        
def up_left(row,col,name):
    reverse_row = row
    flag = False
    reverse_col = col
    row -= 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row >= 0 and col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
                row += 1
            if flag:
                while reverse_row > row and reverse_col > col:
                    box[row][col] = name
                    col += 1
                    row += 1
                break
        
def down_left(row,col,name):
    reverse_row = row
    flag = False
    reverse_col = col
    row += 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row < user and col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
                row -= 1
            if flag:
                while reverse_row < row and reverse_col > col:
                    box[row][col] = name
                    col += 1
                    row -= 1
                break
         
# Change Color only for Computer
def up_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    row = row - 1
    if row < user and row >= 0:
        while row > 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
            elif box[row][col] == name:
                flag = True
                row += 1
            if flag:
                while reverse_row > row:
                    count_computer += 1 
                    row += 1
                break
        
def down_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    row = row + 1
    if row < user and row >= 0:
        while row < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
            elif box[row][col] == name:
                flag = True
                row -= 1
            if flag:
                while reverse_row < row:
                    count_computer += 1 
                    row -= 1
                break
        
def right_computer(row,col,name):
    global count_computer
    reverse_col = col
    flag = False
    col = col + 1
    if col < user and col >= 0:
        while col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
            if flag:
                while reverse_col < col:
                    count_computer += 1 
                    col -= 1
                break
        
def left_computer(row,col,name):
    global count_computer
    reverse_col = col
    flag = False
    col = col - 1
    if col < user and col >= 0:
        while col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
            if flag:
                while reverse_col > col:
                    count_computer += 1 
                    col += 1
                break
        
def up_right_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    reverse_col = col
    row -= 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row >= 0 and col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
                row += 1
            if flag:
                while reverse_row > row and reverse_col < col:
                    count_computer += 1 
                    col -= 1
                    row += 1
                break
        
def down_right_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    reverse_col = col
    row += 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row < user and col < user:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
                col += 1
            elif box[row][col] == name:
                flag = True
                col -= 1
                row -= 1
            if flag:
                while reverse_row < row and reverse_col < col:
                    count_computer += 1 
                    col -= 1
                    row -= 1
                break
        
def up_left_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    reverse_col = col
    row -= 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row >= 0 and col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row -= 1
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
                row += 1
            if flag:
                while reverse_row > row and reverse_col > col:
                    count_computer += 1 
                    col += 1
                    row += 1
                break
        
def down_left_computer(row,col,name):
    global count_computer
    reverse_row = row
    flag = False
    reverse_col = col
    row += 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        while row < user and col >= 0:
            if box[row][col] == ' ':
                break
            elif box[row][col] != name:
                row += 1
                col -= 1
            elif box[row][col] == name:
                flag = True
                col += 1
                row -= 1
            if flag:
                while reverse_row < row and reverse_col > col:
                    count_computer += 1 
                    col += 1
                    row -= 1
                break


# Available Space
def check_up(row,col,name):
    global dict_computer
    row -= 1
    if row < user and row >= 0:
        if box[row][col] == ' ':
            return
        while row >= 0:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row -= 1
            
def check_down(row,col,name):
    global dict_computer
    row += 1
    if row < user and row >= 0:
        if box[row][col] == ' ':
            return
        while row < user:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})         
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row += 1
            
def check_right(row,col,name):
    global dict_computer
    col += 1
    if col < user and col >= 0:
        if box[row][col] == ' ':
            return
        while col < user:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                col += 1
            
def check_left(row,col,name):
    global dict_computer
    col -= 1
    if col < user and col >= 0:
        if box[row][col] == ' ':
            return
        while col >= 0:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f'{row}{col}' : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                col -= 1
        
def check_upright(row,col,name):
    global dict_computer
    row -= 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        if box[row][col] == ' ':
            return
        while row >= 0 and col < user:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row -= 1
                col += 1
            
def check_downright(row,col,name):
    global dict_computer
    row += 1
    col += 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        if box[row][col] == ' ':
            return
        while row < user and col < user:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row += 1
                col += 1
            
def check_downleft(row,col,name):
    global dict_computer
    row += 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        if box[row][col] == ' ':
            return
        while row < user and col >= 0 :
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row += 1
                col -= 1
            
def check_upleft(row,col,name):
    global dict_computer
    row -= 1
    col -= 1
    if (row < user and row >= 0) and (col < user and col >= 0):
        if box[row][col] == ' ':
            return
        while row >= 0 and col >= 0:
            if box[row][col] == ' ':
                print(f"{row} {col}")
                dict_computer.update({f"{row}{col}" : 0})
                break
            if box[row][col] != name:
                break
            if box[row][col] == name:
                row -= 1
                col -= 1
            
# Declare Variable
white = 2
black = 2
name = 'W'

while (black+white < user*user):
    if name == 'B':
        name = 'W'
    else:
        name = 'B'
    
    if name == 'B':
        dict_computer.clear()
        print("\n\n")
        print("\nYou are select only Place : ")
        for i in range(user):
            for j in range(user):
                new_name = name
                if box[i][j] == new_name:
                    if new_name == 'B':
                        new_name = 'W'
                    else:
                        new_name = 'B'
                    check_up(i,j,new_name)
                    check_down(i,j,new_name)
                    check_right(i,j,new_name)
                    check_left(i,j,new_name)
                    check_upright(i,j,new_name)
                    check_upleft(i,j,new_name)
                    check_downright(i,j,new_name)
                    check_downleft(i,j,new_name)
             
        if dict_computer:                            
            # Take User Input
            user1 = input(f"enter the number {name} : ")
            
            user1 = int(user1)
            b = user1 % 10
            user1 = int(user1 / 10)
            a = user1 % 10
            # print(a,b)
        
            box[a][b] = name
        
            # change the color functions
            up(a,b,name)
            down(a,b,name)
            right(a,b,name)
            left(a,b,name)
            up_right(a,b,name)
            up_left(a,b,name)
            down_left(a,b,name)
            down_right(a,b,name)
        
            white = sum(x.count('W') for x in box)
            black = sum(x.count('B') for x in box)
        
            for row in box:
                print(' '.join(row))
            print(f"white is: {white} Black is: {black}")
        
            if white == 0:
                break
            if black == 0:
                break
        
    if name == 'B':
        name = 'W'
    else:
        name = 'B'
        
    dict_computer = {}
    print("\n\n")
    print("Now Turn Computer : ")
    if name == 'W':
        dict_computer.clear()
        for i in range(user):
            for j in range(user):
                new_name = name
                if box[i][j] == new_name:
                    if new_name == 'B':
                        new_name = 'W'
                    else:
                        new_name = 'B'
                    check_up(i,j,new_name)
                    check_down(i,j,new_name)
                    check_right(i,j,new_name)
                    check_left(i,j,new_name)
                    check_upright(i,j,new_name)
                    check_upleft(i,j,new_name)
                    check_downright(i,j,new_name)
                    check_downleft(i,j,new_name)  
         
        if dict_computer:           
            for k in dict_computer.keys():
                user1 = int(k)
                user1 = int(user1)
                b = user1 % 10
                user1 = int(user1 / 10)
                a = user1 % 10
                # print(a,b)
                count_computer = 0
                # counting maximum changes
                up_computer(a,b,name)
                down_computer(a,b,name)
                right_computer(a,b,name)
                left_computer(a,b,name)
                up_right_computer(a,b,name)
                up_left_computer(a,b,name)
                down_left_computer(a,b,name)
                down_right_computer(a,b,name)
                
                dict_computer[f'{a}{b}'] = count_computer
            
            list_computer = []
            max = 0
            for k,v in dict_computer.items():
                if dict_computer[k] > max:
                    max = dict_computer[k]
                    list_computer = k 

            # for k in list_computer:
            print(f"Computer selcte the palce : {list_computer}")
            user1 = int(list_computer)
            user1 = int(user1)
            b = user1 % 10
            user1 = int(user1 / 10)
            a = user1 % 10
                
            box[a][b] = name
        
            # change the color functions
            up(a,b,name)
            down(a,b,name)
            right(a,b,name)
            left(a,b,name)
            up_right(a,b,name)
            up_left(a,b,name)
            down_left(a,b,name)
            down_right(a,b,name)
        
            white = sum(x.count('W') for x in box)
            black = sum(x.count('B') for x in box)
        
            for row in box:
                print(' '.join(row))
            print(f"white is: {white} Black is: {black}")
        
            if white == 0:
                break
            if black == 0:
                break
            
    
# print Result
if white > black:
    print("white winner")
elif white < black:
    print("black winner")
else:
    print("match Draw")             
               