from locust import HttpUser, task, between

class ComparisonUser(HttpUser):
    # ユーザーが次の操作をするまでの待機時間（1〜3秒ランダム）
    wait_time = between(1, 3)

    @task(1)
    def test_monolith(self):
        # モノリス版のエンドポイントを叩く
        # nameを指定することで、結果画面で "Monolith" として集計されます
        self.client.get("http://monolith:8000/buy", name="Monolith /buy")

    @task(1)
    def test_microservices(self):
        # マイクロサービス版のエンドポイントを叩く
        self.client.get("http://order:8000/buy", name="Microservices /buy")