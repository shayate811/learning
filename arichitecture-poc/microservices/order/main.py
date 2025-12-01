import time
import httpx
from fastapi import FastAPI

app = FastAPI()

# Docker Composeのサービス名をホスト名として指定
PAYMENT_URL = "http://payment:8000/pay"
INVENTORY_URL = "http://inventory:8000/check"

@app.get("/buy")
def buy_microservice():
    start_time = time.time()
    
    # ★HTTP通信発生！
    # ここでTCPコネクション確立、データシリアライズなどのオーバーヘッドが乗る
    # verify=False等はPoC用
    with httpx.Client() as client:
        payment = client.get(PAYMENT_URL).json()
        inventory = client.get(INVENTORY_URL).json()

    process_time = (time.time() - start_time) * 1000
    return {
        "architecture": "Microservices",
        "process_time_ms": f"{process_time:.2f}",
        "details": [payment, inventory]
    }