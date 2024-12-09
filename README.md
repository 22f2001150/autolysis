## Running the Script

To generate heatmaps and analyze your data, follow the steps below:

1. **Clone the Repository:**
   Clone the repository to your local system using the following command:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
2. **Install Required Libraries: Ensure that all dependencies are installed by running:**

    pip install -r requirements.txt

3. **Run the Script: Use the uv tool to run the autolysis.py script with your dataset.**

    uv run autolysis.py goodreads.csv
    uv run autolysis.py happiness.csv
    uv run autolysis.py media.csv

4. **Expected Output: After running the above commands, the following outputs will be generated:**

    Heatmap Image Files:

    heatmap_goodreads.png
    heatmap_happiness.png
    heatmap_media.png
   
   These image files will be saved in the working directory, displaying the correlation between different features in the respective datasets.

   **Console Logs: The terminal will display the following logs as the script runs:**

   **Processing goodreads.csv...**
   Generating heatmap for goodreads data...
   Saving heatmap as goodreads_heatmap.png...

   **Processing happiness.csv...**
   Generating heatmap for happiness data...
   Saving heatmap as happiness_heatmap.png...

   **Processing media.csv...**
   Generating heatmap for media data...
   Saving heatmap as media_heatmap.png...

5. **Data Analysis:**

   Correlation between 'Rating' and 'Number of Reviews': 0.87
   Correlation between 'Happiness Score' and 'GDP': 0.65






