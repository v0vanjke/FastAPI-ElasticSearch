from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text as alchemytext
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class PostRubric(Base):
    __tablename__ = 'post_rubric'

    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    rubric_id = Column(Integer, ForeignKey('rubrics.id'), primary_key=True)

    post = relationship("Post", back_populates="rubric")
    rubric = relationship("Rubric")


class Post(Base):
    __tablename__ = 'posts'

    id: int = Column(Integer, primary_key=True, nullable=False)
    text: str = Column(String, nullable=False)
    created_date = Column(TIMESTAMP(timezone=True), server_default=alchemytext('now()'))
    # rubrics: str = Column(String, nullable=False)

    rubrics = relationship('Rubric', secondary='post_rubric', back_populates='post')


class Rubric(Base):
    __tablename__ = 'rubrics'

    id: int = Column(Integer, primary_key=True, nullable=False)
    title: str = Column(String, nullable=False)

    posts = relationship('Post', secondary='post_rubric', back_populates='rubric')

