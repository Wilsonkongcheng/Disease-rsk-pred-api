from fastapi import FastAPI
from dophin_scheduler import main
import asyncio

"""
 启动命令：uvicorn dophin_scheduler_app:app --reload --host 0.0.0.0 --port 80
"""

app = FastAPI()
running = False
message = None


@app.get("/lung")
async def root():
    global running
    running = True
    asyncio.get_event_loop().run_in_executor(None, main)  # 开启线程异步计算
    return {"message": "successfully submit"}


@app.get("/is_complete")
async def is_complete_api():
    global running
    if running:
        return {"is_complete": 'False'}
    else:
        if message:
            return {"is_complete": 'True', "message": message}
        else:
            return {"message": "No start!"}


if __name__ == '__main__':
    pass
