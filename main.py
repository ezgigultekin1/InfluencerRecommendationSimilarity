# main.py

# Import necessary modules and classes.
import os
import nltk
import pandas as pd
import logging
from mongodb_connector import MongoDBConnector
from text_processor import TextProcessor
from influencer_recommender import InfluencerRecommender

# Download NLTK packages.
nltk.download('punkt')
nltk.download('wordnet')

# Configure logging.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

if __name__ == "__main__":
    # Define MongoDB connection details.
    connection_string = 'mongodb://wearisma-read-only:'
    database_name = 'heroku_62fv85nh'

    # Initialize MongoDBConnector and TextProcessor classes.
    connector = MongoDBConnector(connection_string, database_name)
    text_processor = TextProcessor()
    recommender = InfluencerRecommender(connector, text_processor)

    influencers = list(connector.db['influencers'].find({'state': 'active'}).limit(1000))
    text_profiles = recommender.create_text_profiles(influencers)

    queries = ["makeup", "skincare", "fashion", "fitness", "gaming"]
    for query in queries:
        recommendations = recommender.recommend_influencers(query, text_profiles)
        filename = f"{query}_recommendations.csv"
        full_path = os.path.join(os.getcwd(), filename)
        df = pd.DataFrame(recommendations)
        df.to_csv(full_path, index=False)
        logging.info(f"Results saved to {filename} file.")

    # Close MongoDB connection.
    connector.close_connection()