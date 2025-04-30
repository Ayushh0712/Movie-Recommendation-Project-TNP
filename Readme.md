# Movie Recommendation Project – TNP
- A content-based movie recommendation system built using Python and Jupyter Notebook. This project suggests similar movies based on user input by analyzing various features of movies.

### Features

- Content-Based Filtering: Utilizes TF-IDF vectorization and cosine similarity to recommend movies similar to the user's choice.

- Interactive Notebook: Includes a Jupyter Notebook (main.ipynb) that demonstrates the recommendation process step-by-step.

- Python Implementation: Core logic implemented in app.py for modularity and potential integration into larger applications.​

### Technologies Used : 

- Python: Primary programming language for data processing and analysis.

- Jupyter Notebook: For interactive demonstrations and explanations.

- Pandas: Data manipulation and analysis.

- Scikit-learn: Machine learning library used for TF-IDF vectorization and similarity calculations. 

### Project Structure

- Movie Recommendation System
    - app.py
    - main.ipynb
    - movies.csv
    - README.md

1. app.py: 
    - Contains the core functions for processing data and generating recommendations.
2. main.ipynb: 
    - Interactive notebook showcasing the recommendation system in action.
3. movies.csv: 
    - Dataset containing movie information used for generating recommendations

### Getting Started
#### 1. Clone the repository

`git clone https://github.com/Ayushh0712/Movie-Recommendation-Project-TNP.git cd Movie-Recommendation-Project-TNP`

#### 2. Install Dependencies
- Ensure you have Python installed. Then, install the required libraries:

    `pip install pandas scikit-learn`

#### 3. Run the Jupyter Notebook:
- Launch Jupyter Notebook and open main.ipynb to see the recommendation system in action

### How It Works

1. Data Loading: 
    - The system loads movie data from movies.csv.
2. Feature Extraction: 
    - Combines relevant features (like genres, keywords, etc.) into a single string for each movie.
3. Vectorization: 
    - Applies TF-IDF vectorization to convert text data into numerical vectors.
4. Similarity Calculation: 
    - Computes cosine similarity between movie vectors to find similar movies.
5. Recommendation: 
    - Based on the input movie, the system recommends top N similar movies.

### Example
 - If a user inputs the movie "Inception", the system might recommend:​
    - Interstellar
    - The Matrix
    - Memento
    - Shutter Island
    - The Prestige



