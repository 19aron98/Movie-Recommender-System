# 🎥 Movie-Recommender-System
This project implements a content-based recommendation system that recommends movies similar to the input movie title based on textual similarity. The similarity is calculated using cosine similarity on processed movie metadata.

## 🌟 How It Works
* **Data Loading:** Merges movie and credits datasets.
* **Data Processing:** Cleans and preprocesses movie metadata to extract relevant features.
* **Tag Creation:** Combines genres, keywords, cast, crew, and overview into a single `tags` column.
* **Vectorization:** Converts the tags into numerical data using Bag of Words (BOW).
* **Similarity Calculation:** Calculates the cosine similarity between movies.
* **Recommendation:** Recommends 5 movies based on the closest cosine similarity to the input movie.

## 🛠️ How to run?
### STEP 1: Clone the repository
Clone the project repository to your local machine using the following command:
```bash
git clone https://github.com/19aron98/Movie-Recommender-System.git
```

### STEP 2: Create a conda environment after opening the repository
Set up a Python environment using Conda to avoid dependency conflicts:

```bash
conda create -n recommender python -y
conda activate recommender
```

### STEP 3: Install the Dependencies
Install all the necessary Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### STEP 4: Run Web-app
Finally, run the web application library `Streamlit` in the terminal using the below command:

```bash
streamlit run app.py
```