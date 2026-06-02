FROM python:3.11-slim

WORKDIR /docs

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/* \
 && git config --global --add safe.directory /docs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["properdocs", "serve", "--dev-addr=0.0.0.0:8000"]
