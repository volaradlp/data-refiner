from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Base model for SQLAlchemy
Base = declarative_base()


class TweetRefined(Base):
    __tablename__ = "tweets"

    handle = Column(String, nullable=False)
    user_id = Column(String, nullable=False, primary_key=True)
    tweet_id = Column(String, nullable=False, primary_key=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    likes = Column(Integer, nullable=False)
    retweets = Column(Integer, nullable=False)
    replies = Column(Integer, nullable=False)
    quotes = Column(Integer, nullable=False)
    subtweet_id = Column(String, nullable=True)
