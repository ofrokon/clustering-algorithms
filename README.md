# Clustering Algorithms: Unveiling Patterns in Unlabeled Data

This repository contains Python scripts demonstrating various clustering algorithms, from K-Means to Gaussian Mixture Models. It accompanies the Medium post "Clustering Algorithms: Unveiling Patterns in Unlabeled Data".

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Visualizations](#visualizations)
4. [Algorithms Covered](#algorithms-covered)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To run these scripts, you need Python 3.6 or later. Follow these steps to set up your environment:

1. Clone this repository:
   ```
   git clone https://github.com/ofrokon/clustering-algorithms.git
   cd clustering-algorithms
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To generate all visualizations, run:

```
python clustering_algorithms.py
```

This will create PNG files for each clustering algorithm in the current directory.

## Visualizations

This script generates the following visualizations:

1. `kmeans_clustering.png`: Demonstrates K-Means clustering
2. `hierarchical_clustering.png`: Shows a dendrogram from Hierarchical clustering
3. `dbscan_clustering.png`: Illustrates DBSCAN clustering on a non-linear dataset
4. `gmm_clustering.png`: Displays Gaussian Mixture Model clustering

## Algorithms Covered

1. K-Means Clustering
2. Hierarchical Clustering
3. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
4. Gaussian Mixture Models (GMM)

Each algorithm is explained in detail in the accompanying Medium post, including:
- When to use each algorithm
- Pros and cons
- Python implementation using scikit-learn
- Visualization of clustering results

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your suggested changes. If you're planning to make significant changes, please open an issue first to discuss what you would like to change.

## License

This project is open source and available under the [MIT License](LICENSE).

---

For a detailed explanation of these clustering algorithms and their applications, check out the accompanying Medium post: [Clustering Algorithms: Unveiling Patterns in Unlabeled Data](https://medium.com/@mroko001/clustering-algorithms-unveiling-patterns-in-unlabeled-data-20dc15ab090f)

For questions or feedback, please open an issue in this repository.
