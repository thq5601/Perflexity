from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np


class SortSourceService:
    def __init__(self):
        self.embedding_model = SentenceTransformer("all-miniLM-L6-v2")

    def sort_sources(self, query: str, search_results: List[dict]):
        relevant_sources = []
        query_embedding = self.embedding_model.encode(query)

        for res in search_results:
            res_embedding = self.embedding_model.encode(res["content"])

            similarity = float(
                    np.dot(query_embedding, res_embedding)
                    / (np.linalg.norm(query_embedding) * np.linalg.norm(res_embedding))
                )
            
            res['relevance_score'] = similarity
            
            if similarity > 0.5:
                relevant_sources.append(res)

        return sorted(relevant_sources, key=lambda x: x['relevance_score'], reverse=True)