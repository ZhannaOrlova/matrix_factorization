from application.recomender_service import RecommenderService

def main():
    recommender_service = RecommenderService()
    user_id = int(input("Enter user ID to get recommendations: "))
    recommendations = recommender_service.recommend(user_id)

    print(f"Recommended movie IDs for User {user_id}: {recommendations}")

if __name__ == "__main__":
    main()
