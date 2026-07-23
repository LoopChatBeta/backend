from fastapi import FastAPI

app = FastAPI(title="LoopChat API")


@app.get("/")
def root():
    return {"message": "LoopChat API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}
