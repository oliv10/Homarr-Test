from fastapi import FastAPI
import time, logging, asyncio

app = FastAPI()

logger = logging.getLogger(__name__)

sleep_time = 300

async def wait():
    global sleep_time
    for i in range(sleep_time):
        logger.warn(f"No Response Sent for {i} seconds.")
        await asyncio.sleep(1)


@app.get("/admin/api.php")
async def read_root():
    await wait()
    return None

@app.get("/update")
async def update(time: int):
    global sleep_time
    sleep_time = time
    return sleep_time