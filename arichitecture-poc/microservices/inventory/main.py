import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/check")
def check():
    time.sleep(0.05) # 処理時間のシミュレート
    return {"status": "ok", "service": "Inventory Service"}