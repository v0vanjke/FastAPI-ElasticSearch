from api_v1.schemas import PostCreate, ShowPost, RubricCreate, ShowRubric
from api_v1.models import Post, Rubric, PostRubric
from database import async_session
from sqlalchemy import select
from typing import List
from fastapi import HTTPException


class PostRepository:
    # @classmethod
    # async def add_post(cls, post: PostCreate) -> Post:
    #     async with async_session() as session:
    #         data = post.model_dump()
    #         new_post = Post(**data)
    #         session.add(new_post)
    #         await session.commit()
    #         await session.refresh(new_post)
    #         return new_post

    @classmethod
    async def add_post(cls, post: PostCreate) -> Post:
        async with async_session() as session:
            data = post.model_dump()
            new_post = Post(**data)
            post_rubrics = new_post.pop('rubrics')
            session.add(new_post)
            await session.commit()
            await session.refresh(new_post)
            for rubric_id in post_rubrics:
                post_rubric = PostRubric(post_id=data.id, rubric_id=rubric_id)
                session.add(post_rubric)
            await session.commit()
            await session.refresh(new_post)
            return new_post

    @classmethod
    async def delete_post(cls, post_id: int):
        async with async_session() as session:
            post_to_delete = await session.get(Post, post_id)
            if not post_to_delete:
                raise HTTPException(status_code=404, detail="Hero not found")
            await session.delete(post_to_delete)
            await session.commit()
            return f'Post с id = {post_id} удален.'

    @classmethod
    async def get_posts(cls) -> List[ShowPost]:
        async with async_session() as session:
            query = select(Post)
            result = await session.execute(query)
            post_models = result.scalars().all()
            posts = [ShowPost.from_orm(post_model) for post_model in post_models]
            return posts


class RubricRepository:
    @classmethod
    async def add_rubric(cls, rubric: RubricCreate) -> Rubric:
        async with async_session() as session:
            data = rubric.model_dump()
            new_rubric = Rubric(**data)
            session.add(new_rubric)
            await session.commit()
            await session.refresh(new_rubric)
            return new_rubric

    @classmethod
    async def get_rubrics(cls) -> List[ShowRubric]:
        async with async_session() as session:
            query = select(Rubric)
            result = await session.execute(query)
            rubric_models = result.scalars().all()
            rubrics = [ShowRubric.from_orm(rubric_model) for rubric_model in rubric_models]
            return rubrics
