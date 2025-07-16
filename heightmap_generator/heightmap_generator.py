import math
import numpy as np
import matplotlib.pyplot as plt

def euclidean_dist(x1,x2,y1,y2):
    return math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))

def draw_circles(map, circles):
    for x in range(np.shape(map)[0]):
        for y in range(np.shape(map)[1]):
            for center, radius in circles:
                dist_to_center = euclidean_dist(center[0],x,center[1],y)
                if dist_to_center < radius:
                    map[x,y] = int(100 * (1 - (dist_to_center / radius)))

# Global variables
map_scale = 0.25
number_continents = 4
continent_size_range = [100, 400]


map_dimensions = [int(i*map_scale) for i in [7232, 16384]]
heightmap = np.zeros(map_dimensions)
map_x, map_y = np.shape(heightmap)

continents = []
for i in range(number_continents):
    x = np.random.randint(0, high=map_x)
    y = np.random.randint(0, high=map_y)
    size = np.random.randint(continent_size_range[0], continent_size_range[1])
    continent = [[x, y], size]
    continents.append(continent)

draw_circles(heightmap, continents)


imgplot = plt.imshow(heightmap, cmap='gray')
plt.show()