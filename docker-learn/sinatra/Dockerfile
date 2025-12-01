FROM ruby:2.7.6

RUN apt update

RUN apt install -y ruby-dev build-essential libmariadb-dev

WORKDIR /opt/myapp
# 依存解決をキャッシュさせるために先にGemfile系をコピー
COPY Gemfile Gemfile.lock ./
RUN gem install bundler -v 2.4.22 && bundle install
