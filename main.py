from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from database import create_tables, delete_tables
from api_v1.router import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print('База готова')
    yield
    await delete_tables()
    print('База очищена')


app = FastAPI(title='test', lifespan=lifespan)
app.include_router(router_v1)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
