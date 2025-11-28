# 🐳 Docker Learning Sandbox

Docker Compose を用いた、マルチコンテナ構成の検証環境です。
Nginx をリバースプロキシとし、バックエンドの Ruby アプリケーションがデータベースと通信する、一般的な3層Webアーキテクチャを構築しています。

## 📐 Architecture Overview

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#fff', 'edgeLabelBackground':'#fff', 'tertiaryColor': '#f4f4f4'}}}%%
graph LR
    Client([💻 Client Browser]) -- "HTTP Request (Port 80)" --> Nginx

    subgraph "Docker Compose Network (Isolated)"
        direction LR
        Nginx[🚀 nginx<br/>(Web Server / Reverse Proxy)]:::web -- "Proxy Pass (Internal Port)" --> Sinatra[💎 sinatra<br/>(App Server / Ruby)]:::app
        Sinatra -- "SQL Query (Port 3306)" --> MySQL[(🗄️ mysql<br/> Database)]:::db
    end

    %% スタイルの定義
    classDef web fill:#66bb6a,stroke:#2e7d32,color:white,stroke-width:2px;
    classDef app fill:#ef5350,stroke:#c62828,color:white,stroke-width:2px;
    classDef db fill:#42a5f5,stroke:#1565c0,color:white,stroke-width:2px;
