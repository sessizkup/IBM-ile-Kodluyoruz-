def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return distance

points = [(1, 2), (4, 6), (5, 8), (9, 10), (2, 3)]

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

min_distance = min(distances)

print("Noktalar arası mesafeler:", distances)
print("Minimum mesafe:", min_distance)