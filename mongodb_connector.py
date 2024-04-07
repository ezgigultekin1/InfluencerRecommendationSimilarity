# mongodb_connector.py

from pymongo import MongoClient
import logging

class MongoDBConnector:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]

    def fetch_social_media_text(self, influencer):
        texts = []

        # Fetch Instagram media texts
        if 'instagram_user_id' in influencer:
            instagram_texts = self.db.instagram_media.find({
                'user_id': influencer['instagram_user_id'],
                'deleted': {"$ne": True}
            })
            for text in instagram_texts:
                if 'caption' in text:
                    texts.append(text['caption'])

        # Fetch Twitter tweet texts
        if 'twitter_user_id' in influencer:
            twitter_tweets = self.db.twitter_tweets.find({
                'user_id': influencer['twitter_user_id']
            })
            for tweet in twitter_tweets:
                if 'content' in tweet:
                    texts.append(tweet['content'])

        # Fetch YouTube video descriptions
        if 'youtube_channel_id' in influencer:
            youtube_videos = self.db.youtube_videos.find({
                'channel_id': influencer['youtube_channel_id']
            })
            for video in youtube_videos:
                if 'description' in video:
                    texts.append(video['description'])

        if not texts:
            logging.warning(f"No texts found for influencer: {influencer['_id']}")
        return texts

    def close_connection(self):
        self.client.close()
