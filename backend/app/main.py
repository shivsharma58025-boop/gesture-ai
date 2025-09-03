from fastapi import FastAPI, WebSocket
from .api import events

app = FastAPI(title="gesture-ai-backend")

app.include_router(events.router, prefix="/api/events")


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}


@app.websocket("/ws/alerts")
async def alerts_ws(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            msg = await websocket.receive_text()
            await websocket.send_text(f"echo: {msg}")
    except Exception:
        await websocket.close()
