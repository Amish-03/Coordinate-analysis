import cv2
import numpy as np
import csv

def process_full_shape_and_save_coords(path, csv_filename="coordinates.csv", sampling_rate=1):
    # Load and convert image to grayscale
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold to binary (invert so black becomes white in mask)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    coords = []

    # Iterate over every pixel with the given sampling rate
    for y in range(0, binary.shape[0], sampling_rate):
        for x in range(0, binary.shape[1], sampling_rate):
            if binary[y, x] == 255:  # Black region in original image
                coords.append((x, y))
                cv2.circle(img, (x, y), 1, (0, 0, 255), -1)

    # Save coordinates to CSV
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])
        writer.writerows(coords)

    # Show image with sampled points
    cv2.imshow("Full Shape Sampling", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
process_full_shape_and_save_coords(
    r"C:\Users\win10\Desktop\KLE tech\Sem 6\CNC bot\Assets\snail.png",
    r"output_coords.csv",
    sampling_rate=2  # Adjust for density
)
