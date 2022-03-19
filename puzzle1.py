#Print the puzzle states in matrix format
def print_in_format(matrix):
    for i in range(9):
        #print a new line in after every 3 tiles are printed
        if i%3 == 0 and i > 0:
            print("")
        
        #Print the tile
        print(str(matrix[i])+" ", end = "")
 
#-a function that Counts the heuristic value for a state of the 8 puzzle - (Misplaced tiles)
def count(s):
    #-heuristic value counting variable
    c = 0
    
    #~ Solved state of a 8 puzzle for comparison
    ideal = [1, 2, 3,
             4, 5, 6,
             7, 8, 0]
    
    #Loop that iterates through all the tiles of unsolved puzzle and compares them with
    #the solved one's. if they don't match, then increase the heuristic value count by 1
    #~ s is a list
    for i in range(9):
        if s[i] != 0 and s[i] != ideal[i]:
            c += 1
            
    #return the counted heuristic value    
    return c
    # 0 is the blank tile
 
#The movement function that moves the blank tile to possible positions
#and compares the moved states for the minimum heuristic valued state
def move(ar, p, st):
    
    #variable that stores minimum heuristic value of a moved state
    rh = 999999
    
    #Copy the puzzle state to another list variable to be used in here
    store_st = st.copy()
    
    #Loop that makes moves of blank tiles to all possible positions
    for i in range(len(ar)):
        
        #Copying the current puzzle state to another list variable to be
        #used in the swapping blank tile operation
        dupl_st = st.copy()
        
        #swapping the blank tile
        temp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = temp
        
       # f=7
       # y=9
        #f,y = y,f
        
        #counting the heuristic value for swaped puzzle state
        tmp_rh = count(dupl_st)
        
        #if current swaped puzzle state has the less heuristic value than
        #the before one, then store current state and current heuristic value
        if tmp_rh < rh:
            rh = tmp_rh
            store_st = dupl_st.copy()
      
    #return the state with the minimum heuristic value along with the heuristic value
    return store_st, rh
  
#~ Unsolved 8 Puzzle stored in a list 'state'
state = [1, 2, 3, 
         0, 5, 6,
         4, 7, 8]
 
#variable that stores the heuristic value
h = count(state)
#~ count will count the amount of Misplaced tiles
#~ will compare it with a solved one to see how many aren't in correct place
 
#Keeps track of search levels
Level = 1
 
#initial printing of current state of 8 puzzle
print("\n------ Level "+str(Level)+" ------")
print_in_format(state)
print("\nHeuristic Value(Misplaced) : "+str(h))
 
 
#The main loop to find the solution and printing every search level
while h>0:
    #Store the position of the blank tile labeled '0' in the list 'state' 
    pos = int(state.index(0))
    
    #Increasing level as one level of search is executing now
    Level += 1
    
    #if blank tile is in index 0, then possible movement operation
    if pos == 0:
        #array of indexes where blank tile can be moved
        arr = [1, 3]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 1, then possible movement operation
    elif pos == 1:
        #array of indexes where blank tile can be moved
        arr = [0, 2, 4]
        state, h = move(arr, pos, state)
        
    #if blank ile is in index 2, then possible movement operation    
    elif pos==2:
        #array of indexes where blank tile can be moved
        arr = [1, 5]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 3, then possible movement operation
    elif pos==3:
        #array of indexes where blank tile can be moved
        arr = [0, 4, 6]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 4, then possible movement operation
    elif pos==4:
        #array of indexes where blank tile can be moved
        arr = [1, 3, 5, 7]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 5, then possible movement operation
    elif pos==5:
        #array of indexes where blank tile can be moved
        arr = [2, 4, 8]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 6, then possible movement operation
    elif pos==6:
        #array of indexes where blank tile can be moved
        arr = [3, 7]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 7, then possible movement operation
    elif pos==7:
        #array of indexes where blank tile can be moved
        arr = [4, 6, 8]
        state, h = move(arr, pos, state)
        
    #if blank tile is in index 8, then possible movement operation
    elif pos==8:
        #array of indexes where blank tile can be moved
        arr = [5, 6]
        state, h = move(arr, pos, state)
    
    #print current state and heuristic of that state in each search level
    print("\n------ Level "+str(Level)+" ------")
    print_in_format(state)
    print("\nHeuristic Value(Misplaced) : "+str(h)) 