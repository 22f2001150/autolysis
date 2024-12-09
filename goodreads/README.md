# Goodreads Dataset Analysis

This repository contains the analysis of the Goodreads dataset. The project includes generating a heatmap based on correlations within the dataset.

## Dataset Description

The `goodreads.csv` dataset contains various attributes related to books, including ratings, genres, and reviews. The analysis focuses on visualizing relationships and correlations between the dataset features.

## Steps

1. The dataset `goodreads.csv` is loaded and cleaned to remove missing or irrelevant data.
2. A correlation heatmap is generated to visualize relationships between the features in the dataset.
3. The heatmap image is saved as `goodreads.png`.

## Files

- `autolysis.py`: The script that processes the dataset and generates the heatmap.
- `goodreads.csv`: The dataset used for the analysis.
- `goodreads.png`: The heatmap image generated based on the dataset.

## Usage

To run the analysis, you can execute the `autolysis.py` script:

```bash
python autolysis.py /path/to/goodreads.csv

