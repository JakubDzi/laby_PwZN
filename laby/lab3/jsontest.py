from rich.console import Console
import rich.traceback
import json
import gzip

console = Console()
console.clear()
rich.traceback.install()

x = [{i: j for i in range(5)} for j in range(10)]
console.print(x)
console.print(json.dumps(x))

with open('test.json', 'w') as f:
    json.dump(x, f)

with open('test.json', 'r') as f:
    y = json.load(f)
    console.print(y)

with gzip.open('test.json.gzip', 'wt', encoding = 'utf-8') as f:
    json.dump(x, f)

with gzip.open('test.json.gzip', 'rt', encoding = 'utf-8') as f:
    y = json.load(f)
    console.print(y)