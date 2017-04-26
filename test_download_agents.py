import program.download_agents as script
import urllib.request
from io import BytesIO
import json
import argparse

def test_http_return(tmpdir, monkeypatch):
    results = [{
            "age": 84,
            "agreeableness": 0.74
          }
        ]
    
    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    p = tmpdir.mkdir("program").join("agents.json")
    
    # run script
    script.main(["--dest", str(p), "--count", "1"])

    local_res = json.load(open(p))
    assert local_res == script.get_agents(1)
