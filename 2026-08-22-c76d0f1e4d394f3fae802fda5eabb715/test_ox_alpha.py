import urllib.request
req=urllib.request.Request("https://openrouter.ai/stealth/ox-alpha", headers={"User-Agent":"Mozilla/5.0"})
try:
    r=urllib.request.urlopen(req, timeout=10)
    print(r.status)
except Exception as e:
    print(type(e).__name__, str(e))
