#!/usr/bin/env python3
from pathlib import Path
import json
import re

DOC = Path("docs/ASSEMBLER_ORQUESTRACAO_HARDWARE_SOFTWARE.md")
OUT = Path("build/ci-validation")
OUT.mkdir(parents=True, exist_ok=True)
text = DOC.read_text(encoding="utf-8")

required = ["F1", "F2", "F3", "F4", "flowchart TD", "arm64-v8a", "armeabi-v7a"]
missing = [x for x in required if x not in text]

formulas = re.findall(r"\*\*F(\d)\*\*", text)
unique_formulas = sorted(set(formulas))

graph_nodes = re.findall(r"\b([A-H])\[", text)
edges = re.findall(r"([A-H]) --> ([A-H])", text)

result = {
    "document": str(DOC),
    "missing_tokens": missing,
    "formula_count": len(unique_formulas),
    "formulas": [f"F{x}" for x in unique_formulas],
    "node_count": len(set(graph_nodes)),
    "edge_count": len(edges),
    "status": "PASS" if not missing and len(unique_formulas) >= 4 and len(edges) >= 6 else "FAIL",
}

(OUT / "formula_graph_validation.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
(OUT / "formula_graph_edges.txt").write_text("\n".join([f"{a}->{b}" for a,b in edges]), encoding="utf-8")

if result["status"] != "PASS":
    raise SystemExit("Validation failed")
print("Validation PASS")
