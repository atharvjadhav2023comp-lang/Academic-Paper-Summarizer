from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import router

app = FastAPI(
    title="AI Research Paper Summarizer",
    docs_url=None,        # ❌ removes /docs
    redoc_url=None        # ❌ removes /redoc
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
@app.get("/")
def health():
    return "AI Research Paper Summarizer API is running"
