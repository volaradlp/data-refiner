from pydantic import BaseModel


class Tweet(BaseModel):
    handle: str
    user_id: str
    tweet_id: str
    text: str
    likes: int
    retweets: int
    replies: int
    quotes: int
    created_at: int
    subtweet_id: str | None
