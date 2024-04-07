# text_processor.py

import re
import nltk
from nltk.stem import WordNetLemmatizer
import logging

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

class TextProcessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        if not text:
            logging.warning("Empty string provided to preprocess_text.")
            return ""

        # Preprocess the text.
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        tokens = nltk.word_tokenize(text)
        tokens = [token for token in tokens if token not in self.stop_words]
        lemmatized = [self.lemmatizer.lemmatize(token) for token in tokens]

        # Eliminate empty or meaningless text.
        processed_text = ' '.join(lemmatized)
        if not processed_text:
            logging.warning("No content remains after preprocessing.")
            return ""
        return processed_text
