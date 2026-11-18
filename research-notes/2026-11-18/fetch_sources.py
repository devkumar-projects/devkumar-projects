from pathlib import Path
import json, hashlib, urllib.request, urllib.parse
root=Path(__file__).resolve().parent
for item in json.loads((root/'source-download-manifest.json').read_text()):
    target=root/'sources'/item['path']; target.parent.mkdir(parents=True,exist_ok=True)
    content=urllib.request.urlopen(urllib.parse.quote(item['url'],safe=':/'),timeout=90).read()
    assert hashlib.sha256(content).hexdigest()==item['sha256'], item['path']
    target.write_bytes(content)
    print('Verified:',item['path'])
