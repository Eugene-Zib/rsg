import math

lat = 50.603694
lon = 30.650625
center_x = 320
center_y = 256
point_x_center = 558
point_y_center = 328

find_lat = lat + (center_y-point_y_center)*0.38/30.87/3600
find_long = lon + (center_x-point_x_center)*0.38/(math.cos(math.radians(lat))*111/3.6)/3600

print(f'{find_lat},{find_long}')
