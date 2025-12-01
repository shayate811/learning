import time
from fastapi import FastAPI

app = FastAPI()

# --- 擬似的なモジュール（関数呼び出し） ---
def process_payment():
    # DB書き込みなどをシミュレート (50ms)
    time.sleep(0.001)
    return {"status": "paid", "transaction_id": "tx_123"}

def check_inventory():
    # DB読み込みなどをシミュレート (50ms)
    time.sleep(0.001)
    return {"status": "ok", "stock": 99}

# --- エンドポイント ---
@app.get("/buy")
def buy_monolith():
    start_time = time.time()
    
    # ★関数呼び出しなので、ネットワーク遅延ゼロ
    payment = process_payment()
    inventory = check_inventory()
    
    process_time = (time.time() - start_time) * 1000
    return {
        "architecture": "Monolith",
        "process_time_ms": f"{process_time:.2f}",
        "details": [payment, inventory]
    }