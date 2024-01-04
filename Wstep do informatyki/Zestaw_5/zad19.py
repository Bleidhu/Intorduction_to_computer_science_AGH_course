import math
def digit_first(x):
    return x//(10**(math.floor(math.log10(x))))
def digit_last(x):
    return x%10
def czy_ruch_dozwolony(T, x, y, move, targ_x, targ_y):
    if(0 <= x + move[0] < 8 and 0 <= y + move[1] < 8):
        if(digit_first(T[x + move[0]][y + move[1]]) > digit_last(T[x][y])):
            if(abs(targ_x-x) >= abs(targ_x - (x + move[0])) and abs(targ_y-y) >= abs(targ_y - (y + move[1]))):
                return True
    return False
def czy_dojdzie_do_rogu(T, x, y):
    def czy_sie_dostanie(T, x, y, targ_x, targ_y):
        if x == targ_x and y == targ_y:
            return True
        else:
            moves = [(1, 0),(1, 1), (1, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1)]
            for move in moves:
                if czy_ruch_dozwolony(T, x, y, move, targ_x, targ_y):
                    if czy_sie_dostanie(T, x+move[0], y+move[1], targ_x, targ_y):
                        return True
            return False
    return (czy_sie_dostanie(T, x, y, 7, 7) or czy_sie_dostanie(T, x, y, 7, 0) or czy_sie_dostanie(T, x, y, 0, 7))

    
print(czy_dojdzie_do_rogu([[1, 1, 1, 1, 1, 1, 1, 1 ],
[1, 2, 1, 1, 1, 1, 1, 1 ],
[1, 3, 3, 1, 1, 1, 1, 1 ],
[1, 4, 1, 4, 1, 1, 1, 1 ],
[1, 5, 1, 1, 5, 1, 1, 1 ],
[1, 1234567, 1, 1, 1, 6, 1, 1 ],
[1, 2, 1, 1, 1, 1, 7, 1 ],
[1, 3, 4, 5, 6, 7, 8, 9 ]], 0, 0))
