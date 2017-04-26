import program.download_agents as script

import urllib.request

from io import BytesIO
import json

import argparse

def test_http_return(monkeypatch):
    results = [{
            "age": 84,
            "agreeableness": 0.74
          }
        ]
    
    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert script.get_agents(1) == results

def test_main(tmpdir):
    # fake writing file
    p = tmpdir.mkdir("program").join("agents.json")

    script.main(["--dest", 'program/agents-100k.json', "--count", "1"])
