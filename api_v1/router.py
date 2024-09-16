from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api_v1.schemas import ShowPost, PostCreate, RubricCreate, ShowRubric
from database import get_db
from typing import List
from api_v1.repository import PostRepository, RubricRepository


router = APIRouter(
    prefix='/api_v1/posts',
    tags=['Posts']
)


@router.post('')
async def create_post(post: PostCreate, db: AsyncSession = Depends(get_db)) -> PostCreate:
    new_post = await PostRepository.add_post(post)
    return new_post


@router.get('')
async def get_posts() -> List[ShowPost]:
    posts = await PostRepository.get_posts()
    return posts


@router.delete('/{post_id}')
async def get_posts(post_id: int):
    posts = await PostRepository.delete_post(post_id)
    return posts


@router.get('/rubrics')
async def get_rubrics() -> List[ShowRubric]:
    rubrics = await RubricRepository.get_rubrics()
    return rubrics


@router.post('/rubrics')
async def create_post(rubric: RubricCreate) -> RubricCreate:
    new_rubric = await RubricRepository.add_rubric(rubric)
    return new_rubric
