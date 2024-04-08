# Influencer Recommendation System

This project aims to recommend influencers based on textual content similarity across various social media platforms including Instagram, Twitter, and YouTube. It utilizes advanced natural language processing techniques and machine learning models to analyze and predict influencer similarity.

## Project Structure

- `main.py`: The main script that orchestrates the fetching of data, processing, and recommendation logic.
- `influencer_recommender.py`: Contains the `InfluencerRecommender` class responsible for creating text profiles and recommending influencers.
- `mongodb_connector.py`: Defines the `MongoDBConnector` class for managing connections to MongoDB and fetching social media text data.
- `text_processor.py`: Implements the `TextProcessor` class for preprocessing textual data.
- `test_db.py`: A utility script to test the fetching of social media texts for a specific influencer.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- MongoDB database access
- NLTK
- Pandas
- Scikit-learn
- Sentence Transformers

### Installation

1. Clone the repository
2.  Install the required Python packages:

pip install nltk pandas scikit-learn sentence-transformers pymongo

3. Ensure you have access to a MongoDB database containing the necessary social media data.

### Configuration

Edit `mongodb_connector.py` and `main.py` to include your MongoDB connection details:

```python
connection_string = 'mongodb://your_username:your_password@your_host:your_port/your_database'
database_name = 'your_database_name'
Project Description
The project is divided into several key components:

MongoDB Connector: Manages database connections and queries to fetch social media texts.
Text Processor: Cleans and preprocesses the text data for analysis.
Influencer Recommender: Uses NLP and machine learning to create influencer profiles and recommend influencers based on a query.
Testing Script: A utility script to ensure that the MongoDB connector is correctly fetching data.
The main workflow involves fetching influencer data from MongoDB, preprocessing this data, creating textual profiles, and then using cosine similarity to recommend influencers based on a given query.

