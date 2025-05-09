from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String, nullable=True)
    parent_id = Column(Integer, ForeignKey("articles.id"), nullable=True)  # For translations
    language = Column(String, nullable=False, default="ru")
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    author = Column(String, nullable=True)
    source = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())  # Добавлено для отслеживания изменений
    is_top = Column(Boolean, default=False)  # Flag for top news

    category = relationship("Category")
    parent = relationship("Article", remote_side=[id])
