import time
from fastapi import FastAPI
import sys
sys.path.append("../..") # 2階層上を見る
from telemetry import instrument_app

app = FastAPI()
instrument_app(app, service_name="payment-service")

@app.get("/pay")
def pay():
    time.sleep(0.001) # 処理時間のシミュレート
    return {"status": "paid", "service": "Payment Service"}