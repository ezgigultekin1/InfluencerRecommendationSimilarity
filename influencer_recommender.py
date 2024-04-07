# influencer_recommender.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class InfluencerRecommender:
    def __init__(self, connector, text_processor, model_name='sentence-transformers/multi-qa-MiniLM-L6-cos-v1'):
        self.connector = connector
        self.text_processor = text_processor
        self.model = SentenceTransformer(model_name)

    def create_text_profiles(self, influencers):
        text_profiles = []
        for influencer in influencers:
            texts = self.connector.fetch_social_media_text(influencer)
            combined_text = " ".join(texts)

            if combined_text:
                preprocessed_text = self.text_processor.preprocess_text(combined_text)
                profile_vector = self.model.encode(preprocessed_text)
                text_profiles.append({
                    'influencer_id': influencer['_id'],
                    'text_profile': preprocessed_text,
                    'profile_vector': profile_vector
                })
            else:
                print(f"No content to process for influencer: {influencer['_id']}")

        return text_profiles

    def recommend_influencers(self, query, text_profiles, top_n=5):
        query_embedding = self.model.encode(self.text_processor.preprocess_text(query))
        recommendations = []
        for profile in text_profiles:
            similarity = cosine_similarity([query_embedding], [profile['profile_vector']])[0][0]
            recommendations.append({'influencer_id': profile['influencer_id'], 'similarity': similarity})

        # Sort influencers based on highest similarity and return top_n
        sorted_recommendations = sorted(recommendations, key=lambda x: x['similarity'], reverse=True)[:top_n]
        return sorted_recommendations
