import asyncio
from contextlib import asynccontextmanager
from time import monotonic

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class TestResponse(BaseModel):
    elapsed: float


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.lock = asyncio.Lock()
    yield

app = FastAPI(lifespan=lifespan)


async def work() -> None:
    await asyncio.sleep(3)


@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()
    async with app.lock:
        await work()
    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)


if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0",
                port=80)