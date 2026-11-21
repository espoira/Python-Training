cells = int(input())
coords = []
x = 10**9
y = 10**9
left_x, bottom_y, right_x, top_y = [x, y, -x, -y]

for i in range(cells):
    coords.append(list(map(int, input().split())))
    if (coords[i][0] < left_x):
        left_x = coords[i][0]
    if (coords[i][0] > right_x):
        right_x = coords[i][0]
    if (coords[i][1] > top_y):
        top_y = coords[i][1]
    if (coords[i][1] < bottom_y):
        bottom_y = coords[i][1]

print(left_x, bottom_y, right_x, top_y)