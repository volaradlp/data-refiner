from typing import Dict, Any, List
from refiner.models.refined import Base
from refiner.transformer.base_transformer import DataTransformer
from refiner.models.refined import TweetRefined
from refiner.models.unrefined import Tweet
from datetime import datetime


class TweetTransformer(DataTransformer):
    """
    Transformer for tweet data as defined in the example.
    """

    def transform(self, data: list[Dict[str, Any]]) -> List[Base]:
        """
        Transform raw tweet data into SQLAlchemy model instances.

        Args:
            data: Dictionary containing tweet data

        Returns:
            List of SQLAlchemy model instances
        """
        models = []
        # Validate data with Pydantic
        for tweet in data:
            unrefined_tweet = Tweet.model_validate(tweet)

            # Create user instance
            tweet = TweetRefined(
                handle=unrefined_tweet.handle,
                user_id=unrefined_tweet.user_id,
                tweet_id=unrefined_tweet.tweet_id,
                text=unrefined_tweet.text,
                created_at=datetime.fromtimestamp(unrefined_tweet.created_at),
                likes=unrefined_tweet.likes,
                retweets=unrefined_tweet.retweets,
                replies=unrefined_tweet.replies,
                quotes=unrefined_tweet.quotes,
                subtweet_id=unrefined_tweet.subtweet_id,
            )
            models.append(tweet)

        return models
