import pandas as pd
import warnings
import ast
import requests
from src.secret_key import Movie_API
from nltk.stem.porter import PorterStemmer

warnings.filterwarnings("ignore")


# Instances
ps = PorterStemmer()

# Basic preprocessing
def basic_preprocess(data: pd.DataFrame) -> pd.DataFrame:
    """Cleans a DataFrame by removing missing values and duplicates."""

    # Drop missing values if any exist
    if data.isna().sum().sum() > 0:  # sum().sum() ensures checking across all columns
        data = data.dropna()

    # Drop duplicate values if any exist
    if data.duplicated().sum() > 0:
        data = data.drop_duplicates()

    return data

# Advance preprocessing
def clean(obj):
    """Returns a clean list of Names from a string object"""

    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def extract_top3_cast(obj) -> list:
    """Returns Top 3 Cast names from a string object"""

    L = []
    for i, j in enumerate(ast.literal_eval(obj)):
        L.append(j['name'])
        if i == 2:
            break
    return L

def extract_crew_director(obj) -> list:
    """Returns the Director name from a string object"""

    L = []
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
    return L

def stem(text):
    """Returns the text with basic"""

    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={Movie_API}")
    poster_data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + poster_data['poster_path']