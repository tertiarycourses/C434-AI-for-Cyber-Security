import importlib.util
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'solution'/'engine.py'
spec=importlib.util.spec_from_file_location('engine',P); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def test_solution():
    import csv, json
    root=Path(__file__).resolve().parents[1]
    assert m.run(3) is not None
    assert (root/'evidence'/'result.json').exists()
    assert (root/'tool-exercise.md').exists()
    assert len([p for p in (root/'mock-data').iterdir() if p.is_file() and p.name!='README.md']) >= 3
    expected=['phishing_triage.csv']
    for name in expected:
        path=root/'evidence'/name
        assert path.exists() and path.stat().st_size>20, name
        if path.suffix=='.json': assert json.loads(path.read_text()) is not None
        elif path.suffix=='.csv': assert list(csv.DictReader(path.open()))
        elif path.suffix=='.md': assert path.read_text().startswith('# ') and 'Human review' in path.read_text()
