import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai

# Replace this with your actual AIPROXY token and endpoint
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjIwMDExNTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.ONnXC8A1F9s9311O9whewBvbGDz1CLdx6HgJEe2gjn0'
openai.api_base = 'https://aiproxy.sanand.workers.dev/openai/'

# Function to generate a correlation heatmap
def generate_heatmap(dataset_name, df):
    # Drop non-numeric columns for correlation calculation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Check if there are any numeric columns to calculate correlation
    if numeric_df.empty:
        print(f"No numeric columns found in {dataset_name}. Skipping heatmap generation.")
        return
    
    # Create the directory if it doesn't exist
    directory = f"/content/{dataset_name}"
    os.makedirs(directory, exist_ok=True)
    
    # Calculate correlation and generate heatmap
    plt.figure(figsize=(10, 8))
    correlation_matrix = numeric_df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    heatmap_filename = f"{directory}/heatmap.png"
    plt.savefig(heatmap_filename)
    plt.close()
    print(f"Heatmap saved as {heatmap_filename}")

# Function to generate narrative from the dataset analysis
def generate_narrative(dataset_name, summary):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=f"Summarize the following dataset analysis for {dataset_name}:\n{summary}",
            max_tokens=150
        )
        narrative = response.choices[0].text.strip()
        print("Generated Story:\n", narrative)
    except Exception as e:
        print(f"Error generating story: {str(e)}")

# Function to analyze the dataset
def analyze_dataset(dataset_name, dataset_path):
    # Load the dataset
    try:
        df = pd.read_csv(dataset_path)
        print(f"Dataset {dataset_name} loaded successfully.")
    except Exception as e:
        print(f"Error loading dataset {dataset_name}: {str(e)}")
        return
    
    # Perform basic analysis
    print(f"\nBasic Analysis for {dataset_name}:")
    print(f"Shape of the dataset: {df.shape}")
    print(f"Columns: {df.columns}")
    print(f"Missing Values: \n{df.isnull().sum()}")
    print(f"Summary Statistics: \n{df.describe()}")
    
    # Generate the heatmap
    generate_heatmap(dataset_name, df)
    
    # Generate the narrative
    summary = f"Dataset Shape: {df.shape}, Columns: {list(df.columns)}, Missing Values: {df.isnull().sum().to_dict()}, Summary Statistics: {df.describe().to_dict()}"
    generate_narrative(dataset_name, summary)

# Main function to run the analysis
def main():
    # Specify the datasets and their paths
    datasets = {
        'goodreads': '/content/sample_data/goodreads.csv',
        'happiness': '/content/sample_data/happiness.csv',
        'media': '/content/sample_data/media.csv'
    }

    for dataset_name, dataset_path in datasets.items():
        print(f"\nAnalyzing {dataset_name} dataset...")
        analyze_dataset(dataset_name, dataset_path)

if _name_ == "_main_":
    main()
