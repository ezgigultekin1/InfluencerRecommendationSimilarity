# test_db.py
from mongodb_connector import MongoDBConnector

# MongoDB connection
connection_string = 'mongodb://wearisma-read-only:'
database_name = 'heroku_62fv85nh'

# test influencer_id
some_influencer_id = '5660be520571bb0300b20f13'

# Create an instance of the MongoDBConnector class.
connector = MongoDBConnector(connection_string, database_name)

# Fetch Instagram media texts for a specific influencer.
instagram_texts = connector.fetch_social_media_text({'instagram_user_id': some_influencer_id})

# Check the content of the fetched data.
print(instagram_texts)