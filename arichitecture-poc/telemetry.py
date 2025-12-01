from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

def instrument_app(app, service_name):
    # 1. トレーサーのプロバイダー設定
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    
    # 2. Jaeger (OTLP) へのエクスポーター設定
    # docker-composeで指定する "jaeger" ホストの4317ポートへ送信
    exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)
    
    # 3. プロセッサー追加
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)

    # 4. 自動計装の適用
    # FastAPIのリクエストを自動でトレース
    FastAPIInstrumentor.instrument_app(app, tracer_provider=provider)
    # httpx（外部通信）も自動でトレース
    HTTPXClientInstrumentor().instrument(tracer_provider=provider)