best_pos_coords_y = -1
best_pos_coords_x = -1
best_pos_value_1D = -100
terra_1D = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,3,0,1,0,3,2,0,1,0,0,0,0,0,0,0],
            [0,0,0,3,0,0,1,0,2,1,0,0,3,0,0,0],
            [0,0,0,8,7,0,0,0,1,0,0,4,6,8,0,0],
            [0,0,3,9,3,0,0,0,0,0,0,0,1,0,0,0],
            [0,0,0,2,0,0,0,5,4,2,0,0,0,0,0,0],
            [0,0,0,0,0,0,6,9,8,9,0,0,1,3,0,0],
            [0,0,0,2,3,2,0,6,9,7,3,0,0,2,0,0],
            [0,1,0,0,0,0,0,0,0,3,0,1,3,1,0,0],
            [0,0,0,0,1,0,0,0,0,0,0,0,2,1,0,0],
            [0,0,1,3,2,1,0,1,4,2,0,0,0,0,0,0],
            [0,0,0,0,8,1,0,0,3,0,0,7,4,0,0,0],
            [0,0,0,2,9,4,0,0,0,0,0,2,5,7,0,0],
            [0,1,0,0,1,1,0,3,1,0,0,0,7,0,0,0],
            [0,2,1,0,0,0,0,2,4,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]

print (terra_1D);
def WayFiender_1D(pos_x,pos_y, HP):
    global best_pos_coords_y
    global best_pos_coords_x
    global best_pos_value_1D
    global terra_1D
    
    calculation = HP + terra_1D[pos_x][pos_y]
    if (calculation > best_pos_value_1D ):
        best_pos_coords_x = pos_x
        best_pos_coords_y = pos_y
        best_pos_value_1D = calculation

    if (HP > 0):
        if (pos_x > 0):
            WayFiender_1D(pos_x -1,pos_y, HP-1)

        if (pos_x < (len(terra_1D[1])-1)):
            WayFiender_1D(pos_x +1,pos_y, HP-1)
      
        if (pos_y > 0):
            WayFiender_1D(pos_x, pos_y -1, HP -1)

        if (pos_y < (len(terra_1D[1])-1)):
            WayFiender_1D(pos_x ,pos_y+1, HP-1)

start_pos_x = int(input("Введите стартовую позицию x: "))
start_pos_y = int(input("Введите стартовую позицию y: "))
start_turns = 7
best_pos_coords_y = -1
best_pos_coords_x = -1
best_pos_value_1D = -100
WayFiender_1D(start_pos_x, start_pos_y, start_turns)
print("Координаты позиции:","(позиция по y)",best_pos_coords_x,"(позиция по x)", best_pos_coords_y)
print("Значение клетки:",terra_1D[best_pos_coords_x ][best_pos_coords_y])
print("Общий профит:",best_pos_value_1D)
