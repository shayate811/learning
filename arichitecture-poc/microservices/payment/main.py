import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/pay")
def pay():
    time.sleep(0.05) # 処理時間のシミュレート
    return {"status": "paid", "service": "Payment Service"}