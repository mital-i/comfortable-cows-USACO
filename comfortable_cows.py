#input stuff
num_cows = int(input())
cow_coords = []

for i in range(num_cows): 
    coordinates = input().split()
    coordinates[0] = int(coordinates[0])
    coordinates[1] = int(coordinates[1])
    cow_coords.append(coordinates)
    
#find the coordinates you need to add a cow to in order to make the initial cows uncomfortable
def find_num_need_to_add(coords_list, i): 
    
    #brute force method lol
    num_adjacent = 0
    current_coord = coords_list[i]
    not_adjacent = []
    
    coord_up = [current_coord[0], current_coord[1] + 1]
    coord_down = [current_coord[0], current_coord[1] - 1]
    coord_left = [current_coord[0] - 1, current_coord[1]]
    coord_right = [current_coord[0] + 1, current_coord[1]]
    
    if coord_up in coords_list: 
        num_adjacent+=1
    elif coord_up not in coords_list: 
        not_adjacent.append(coord_up)
        
    if coord_down in coords_list: 
        num_adjacent+=1 
    elif coord_down not in coords_list: 
        not_adjacent.append(coord_down)
        
    if coord_left in coords_list: 
        num_adjacent+=1 
    elif coord_left not in coords_list: 
        not_adjacent.append(coord_left)
        
    if coord_right in coords_list: 
        num_adjacent+=1
    elif coord_right not in coords_list: 
        not_adjacent.append(coord_right)
        
    if num_adjacent == 3: 
        coords_list.append(not_adjacent)
        
    return coords_list

#how do I write the code so that it continously goes through every cow until all cows are comfortable? 
#right now it only checks for the cows initially inputted


#just to test the function
print(find_num_need_to_add(cow_coords, 5))

