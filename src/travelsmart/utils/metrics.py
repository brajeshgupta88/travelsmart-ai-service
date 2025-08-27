from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("travelsmart_request_count", "number of requests", ["path", "method", "status"])
REQUEST_LATENCY = Histogram("travelsmart_request_latency_seconds", "request latency", ["path"])
