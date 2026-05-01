from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.result import router as result_router
from app.routes.visualize import router as visualize_router

app = FastAPI()
app.include_router(chat_router)
app.include_router(result_router)
app.include_router(visualize_router)