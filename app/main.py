from fastapi import FastAPI


app = FastAPI(title="PR Assistant (dev)")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"msg": "PR Assistant - dev server"}