# Monolith vs Microservices PoC

**「マイクロサービス化による通信オーバーヘッド（レイテンシの税金）は実際どれくらいなのか？」**

この疑問を検証するために、Python (FastAPI) と Docker を用いて構築した比較検証用プロジェクトです。

<br>

**📖 検証結果の詳細な解説記事 (Zenn)**
👉 [【検証】モノリス vs マイクロサービス：通信オーバーヘッドという「税金」を実測してみた](https://zenn.dev/shayate811/articles/monolith-vs-microservices)

---

## ⚡️ アーキテクチャの比較概要

本PoCでは、純粋な「通信コスト」の差を測定するため、ビジネスロジックの処理時間を極小（**1ms**）に設定しています。

* **モノリス構成:** すべての処理を単一のプロセス内で関数呼び出しとして実行。
* **マイクロサービス構成:** 処理を複数のコンテナに分割し、HTTP通信で連携。

## 🛠 技術スタック

| Category | Tech | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.11 | 軽量なベースイメージを使用 |
| **Framework** | FastAPI | 高速な非同期Webフレームワーク |
| **Infra** | Docker Compose | 複数コンテナのオーケストレーション |
| **Load Testing** | Locust | Pythonでシナリオが書ける負荷試験ツール |
| **Tracing** | Jaeger (OpenTelemetry) | 分散トレーシングによるボトルネック可視化 |

## 🚀 実行方法

Docker Desktopが起動している状態で、以下のコマンドを実行してください。

### 1. 起動

```bash
# リポジトリのクローン（まだの場合）
git clone [https://github.com/shayate811/learning.git](https://github.com/shayate811/learning.git)
cd learning/arichitecture-poc

# コンテナのビルドと起動
docker-compose up -d --build
```

### 2. アクセス

起動後、以下のURLで各ツールにアクセスできます。

・Locust (負荷試験管理画面): http://localhost:8089

・Jaeger (トレーシング画面): http://localhost:16686

・モノリス API: http://localhost:8001/buy

・マイクロサービス API (Order): http://localhost:8002/buy

### 3. 停止

検証が終わったら、以下のコマンドでコンテナを停止・削除します。

```bash
docker-compose down
```

---
## 📂 ディレクトリ構成

```
.
├── docker-compose.yml      # 全体の構成定義
├── telemetry.py            # OpenTelemetry(Jaeger)共通設定
├── locustfile.py           # 負荷試験シナリオ
├── monolith/               # モノリス版ソースコード
└── microservices/
    ├── order/              # 注文サービス (Gateway役割)
    ├── payment/            # 決済サービス
    └── inventory/          # 在庫サービス
```

