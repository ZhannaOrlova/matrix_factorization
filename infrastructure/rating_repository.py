import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

class RatingRepository:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.csv_file = os.getenv('CSV_FILE_PATH')  # Get the CSV file path from the environment variable

    def load_ratings(self):
        # Load the CSV file from the specified path
        print("Loading CSV file...")
        df = pd.read_csv(self.csv_file)

        # Check if expected columns are present
        required_columns = ['userId', 'movieId', 'rating']
        if not all(col in df.columns for col in required_columns):
            raise KeyError("Expected columns 'userId', 'movieId', 'rating' not found in DataFrame")

        print(f"DataFrame shape: {df.shape}")
        print("Columns in DataFrame:", df.columns)

        # Limit the DataFrame to the first 1,000 rows for testing
        df = df.head(1000)
        print(f"Reduced DataFrame shape: {df.shape}")

        # Select a sample of unique movie IDs
        print("Sampling movie IDs...")
        unique_movie_ids = df['movieId'].unique()
        num_samples = min(10000, len(unique_movie_ids))

        # Randomly sample movie IDs
        sample_movie_ids = pd.Series(unique_movie_ids).sample(n=num_samples, random_state=42)

        # Filter the DataFrame to include only the selected movies
        df_sampled = df[df['movieId'].isin(sample_movie_ids)]
        print(f"Sampled DataFrame shape: {df_sampled.shape}")

        # Create a user-item ratings matrix from the sampled data
        print("Creating ratings matrix...")
        ratings_matrix = df_sampled.pivot(index='userId', columns='movieId', values='rating').fillna(0).values
        
        print("Ratings matrix created successfully!")
        
        # Create a mapping from userId to index
        user_id_mapping = {user_id: index for index, user_id in enumerate(df_sampled['userId'].unique())}
        return ratings_matrix, user_id_mapping

# Test the RatingRepository
if __name__ == "__main__":
    repo = RatingRepository()
    try:
        ratings_matrix, user_id_mapping = repo.load_ratings()
        print("Ratings Matrix shape:", ratings_matrix.shape)
        print("User ID Mapping:", user_id_mapping)  # Optional, for debugging
    except Exception as e:
        print(f"An error occurred: {e}")
