import urllib.request


with urllib.request.urlopen("http://127.0.0.1:8080/health", timeout=5) as response:
    if response.status != 200 or response.read() != b"ok":
        raise SystemExit("health response mismatch")
