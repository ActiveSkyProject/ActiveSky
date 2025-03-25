import unittest
from website.views import ActivityRecommendation

class ActivityRecommendationTest(unittest.TestCase):
    def test_temperature_recommendations(self):
        """Test if temperature-based activity recommendations work correctly"""
        # Test hot weather 
        hot_recommender = ActivityRecommendation(35, "clear")
        hot_activity = hot_recommender.recommend_activity_based_on_temperature()
        self.assertIsNotNone(hot_activity)

        # Test moderate weather
        moderate_recommender = ActivityRecommendation(25, "clear")
        moderate_activity = moderate_recommender.recommend_activity_based_on_temperature()
        self.assertIsNotNone(moderate_activity)

        # Test cool weather
        cool_recommender = ActivityRecommendation(15, "clear")
        cool_activity = cool_recommender.recommend_activity_based_on_temperature()
        self.assertIsNotNone(cool_activity)

        # Test cold weather
        cold_recommender = ActivityRecommendation(5, "clear")
        cold_activity = cold_recommender.recommend_activity_based_on_temperature()
        self.assertIsNotNone(cold_activity)

    def test_weather_condition_recommendations(self):
        """Test if weather condition-based activity recommendations work correctly"""
        # Test different weather conditions
        conditions = ["rain", "snow", "clear", "cloud", "fog", "storm", "other"]

        for condition in conditions:
            recommender = ActivityRecommendation(20, condition)
            activity = recommender.recommend_activity_based_on_weather()
            self.assertIsNotNone(activity)

    def test_time_based_recommendations(self):
        """Test if time-based activity recommendations work correctly"""
        recommender = ActivityRecommendation(20, "clear")
        activity = recommender.recommend_activity_based_on_time()
        self.assertIsNotNone(activity)

if __name__ == '__main__':
    unittest.main()