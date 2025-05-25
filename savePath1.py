import csv
import math
import matplotlib.pyplot as plt

def read_coordinates(csv_file):
    points = []
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            x, y = float(row[0]), float(row[1])
            points.append((x, y))
    return points

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def nearest_neighbor_tsp(points):
    if not points:
        return []
    unvisited = points[:]
    path = [unvisited.pop(0)]  # Start with the first point
    while unvisited:
        last = path[-1]
        next_point = min(unvisited, key=lambda p: euclidean_distance(last, p))
        path.append(next_point)
        unvisited.remove(next_point)
    return path

def write_path_to_csv(path, filename="path.csv"):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])  # Header
        for x, y in path:
            writer.writerow([x, y])
    print(f"Path written to {filename}")

def plot_path(path):
    plt.figure(figsize=(8, 8))
    x_vals = [p[0] for p in path]
    y_vals = [100 - p[1] for p in path]  # Invert Y for display

    plt.scatter(x_vals, y_vals, c='blue')
    for i in range(len(path) - 1):
        start = path[i]
        end = path[i + 1]
        plt.arrow(start[0], 100 - start[1], end[0] - start[0], -(end[1] - start[1]),
                  head_width=1, length_includes_head=True, color='red')
    plt.scatter(path[0][0], 100 - path[0][1], c='green', s=100, label='Start')
    plt.scatter(path[-1][0], 100 - path[-1][1], c='orange', s=100, label='End')

    plt.title('Optimized Drawing Path')
    plt.xlabel('X')
    plt.ylabel('Y (Inverted)')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    points = read_coordinates('output_coords.csv')
    optimized_path = nearest_neighbor_tsp(points)
    write_path_to_csv(optimized_path, 'path.csv')
    plot_path(optimized_path)

if __name__ == "__main__":
    main()
