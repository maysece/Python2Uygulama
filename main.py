points = [(2,5), (4,5),(8,3),(-4,0)]
distances = list()

def euclideanDistance(point1:tuple, point2:tuple) -> float:
    return pow(pow(point1[0]-point2[0], 2) + pow(point1[1] - point2[1], 2), .5)

for i0 in range(len(points)-1):
    for i1 in range(i0+1, len(points)):
        distances.append(euclideanDistance(point1=points[i0], point2=points[i1]))

min_distance = distances[0]
for d in distances:
    min_distance = min(d, min_distance)

print(min_distance)



