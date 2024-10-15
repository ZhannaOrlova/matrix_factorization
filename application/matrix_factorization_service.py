import numpy as np

class MatrixFactorization:
    def __init__(self, ratings, num_features=2, learning_rate=0.01, regularization=0.02, num_iterations=5000):
        self.ratings = ratings
        self.num_users, self.num_items = ratings.shape
        self.num_features = num_features
        self.learning_rate = learning_rate
        self.regularization = regularization
        self.num_iterations = num_iterations
        self.user_features = np.random.normal(scale=1./self.num_features, size=(self.num_users, self.num_features))
        self.item_features = np.random.normal(scale=1./self.num_features, size=(self.num_items, self.num_features))

    def train(self):
        for _ in range(self.num_iterations):
            for i in range(self.num_users):
                for j in range(self.num_items):
                    if self.ratings[i, j] > 0:  # Only train on non-zero ratings
                        prediction = self.predict(i, j)
                        error = self.ratings[i, j] - prediction
                        self.user_features[i, :] += self.learning_rate * (error * self.item_features[j, :] - self.regularization * self.user_features[i, :])
                        self.item_features[j, :] += self.learning_rate * (error * self.user_features[i, :] - self.regularization * self.item_features[j, :])

    def predict(self, user_id, item_id):
        return np.dot(self.user_features[user_id, :], self.item_features[item_id, :])
