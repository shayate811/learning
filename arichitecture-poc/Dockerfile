FROM python:3.11-slim

WORKDIR /app

# ライブラリのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードはdocker-composeでマウントするので、ここではCMDのみ定義
# (デフォルトコマンド。compose側で上書き可能)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]