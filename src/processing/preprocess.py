######################################################################
#                                                                    #
#      Copyright © 2023 Marcus Antonelli. All Rights Reserved.       #
#                                                                    # 
#      Licensed under the GNU General Public License v3, a free      #
#     copyleft license with minimal stipulations and limitations.    #
#                Obtain a copy of the license below:                 #
#                                                                    #
#             http://gnu.org/licenses/gpl-3.0.en.html                #
#                                                                    #
######################################################################
#                            DISCLAIMER                              #
######################################################################
#                                                                    #
#        This software, like any other GPLv3 licensed works,         #
#    is provided "as is". There is no warranty, either expressed     #
#      or implied. Unless required by law or explicity written,      #
#   the author of this software is under no obligation to accept     #
#       liability for damages caused by the usage of this file.      #
#                                                                    #
#   See the full license for further information and more detailed   #
#                     explanations and language.                     #
#                                                                    #
######################################################################

import contractions
import string
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from typing import Generator
        
class Chunk:

    def __init__(self):
        self.tkn_reviews = []
        self.topics = []

    def spit_review(self):
        for review in self.tkn_reviews:
            yield review

    def add_review(self, review):
        self.tkn_reviews.append(review)


def preprocess(reviews: list[str], chunk_size = 16) -> list[Chunk]:

    processed_count = 0
    current_chunk = Chunk()

    for review in reviews:

        if len(review) < 4:
            break

        review = expand_contractions(review)
        review = remove_punctuation(review) 
        tokenized_review = tokenize(review) 
        tokenized_review = remove_stopwords(tokenized_review) # ['that', 'cool']

        current_chunk.add_review(tokenized_review)
        processed_count += 1

        if processed_count == chunk_size: # create chunks that are max 16 reviews in size
            yield current_chunk
            current_chunk = Chunk()
            processed_count = 0
            
    if processed_count != 0:
        yield current_chunk 


def expand_contractions(text: str) -> str:
    return contractions.fix(text)

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))

def tokenize(text: str) -> list[str]:
    return word_tokenize(text.lower())

def remove_stopwords(review_tokens: list[str]) -> list[str]:
    stop_words = set(stopwords.words('english'))
    return [token for token in review_tokens if token not in stop_words]
