# app/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="PR Assistant (Standard)", version="0.1.0")

@app.get("/health")
def health():
    return JSONResponse({"status": "ok"})

# نمونه endpoint ساده برای تست webhook payload
@app.post("/webhook")
async def webhook(payload: dict):
    # فقط برای تست: ذخیرهٔ payload یا لاگ کردن
    return {"received": True, "keys": list(payload.keys())}
