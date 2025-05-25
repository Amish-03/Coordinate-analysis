# Coordinate-analysis
# 🖼️➡️📈➡️✍️ Image to Optimized Drawing Path

This repository contains code to:

1. Take a **black and white image** as input.
2. Analyze **black pixels** and extract their coordinates.
3. Save those coordinates into a CSV file.
4. Find an **optimized drawing path** through those coordinates.
5. Save the optimized path into another CSV file.

---

## 🔧 Files

### `pixelScan.py`
- **Purpose**: Scans an image for black pixels and stores their coordinates.
- **Output**: `output_coords.csv`

### `savePath.py`
- **Purpose**: Takes coordinates from `output_coords.csv` and optimizes the drawing path using a greedy TSP algorithm.
- **Output**: `path.csv`

---

## ✅ Requirements

- Python 3.x
- OpenCV → `pip install opencv-python`
- NumPy → `pip install numpy`

---

## ▶️ How to Use

1. **Run pixelScan** to extract black pixel coordinates:
   ```bash
   python pixelScan.py

