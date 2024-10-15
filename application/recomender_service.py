from infrastructure.rating_repository import RatingRepository  # Corrected import
from application.matrix_factorization_service import MatrixFactorization

class RecommenderService:
    def __init__(self):
        self.rating_repo = RatingRepository()
        self.ratings, self.user_id_mapping = self.rating_repo.load_ratings()  # Load ratings and user mapping
        self.model = MatrixFactorization(self.ratings)

    def recommend(self, user_id):
        if user_id not in self.user_id_mapping:
            raise ValueError(f"User ID {user_id} not found in the user mapping.")

        user_index = self.user_id_mapping[user_id]  # Get the index for the user ID
        predictions = self.model.user_features[user_index, :].dot(self.model.item_features.T)
        return predictions

