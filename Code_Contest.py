import re
import sys
import time
import math
import os
import tempfile
import subprocess
import requests
from pathlib import Path

# =========================================================
# Redirect ALL output to file
# =========================================================
OUTPUT_FILE = "codellama_13b_output.txt"
sys.stdout = open(OUTPUT_FILE, "w", encoding="utf-8")

# =========================================================
# Code cleaner (UNCHANGED)
# =========================================================
def extract_clean_code(generated_text: str) -> str:
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)\s*```", generated_text, re.DOTALL)
    if code_blocks:
        return max(code_blocks, key=len).strip()

    lines = generated_text.splitlines()
    code_started = False
    code_lines = []
    for line in lines:
        if not code_started and line.lstrip().startswith(
            ("def ", "class ", "import ", "from ")
        ):
            code_started = True
        if code_started:
            code_lines.append(line)

    if code_lines:
        return "\n".join(code_lines).strip()

    return generated_text.strip()

# =========================================================
# Ollama generation
# =========================================================
def generate_with_local_ollama(problem_description: str) -> str:
    url = "http://127.0.0.1:11434/api/generate"
    model = "codellama:13b"

    system_msg = (
        "You are a competitive programming assistant.\n"
        "Write a COMPLETE Python 3 program.\n"
        "- Read from standard input\n"
        "- Write to standard output\n"
        "- Output ONLY code\n"
    )

    payload = {
        "model": model,
        "prompt": system_msg + "\nProblem:\n" + problem_description,
        "num_predict": 700,
        "temperature": 0.1,
        "stream": False,
    }
    # 0= temp
    # deterministic = True

    resp = requests.post(url, json=payload, timeout=300)
    resp.raise_for_status()
    return extract_clean_code(resp.json().get("response", ""))

# =========================================================
# Load problems
# =========================================================
ROOT = Path("code_contests_165")
problems = []

for folder in sorted(p for p in ROOT.iterdir() if p.is_dir()):
    desc = folder / "description.txt"
    inp = folder / "input"
    out = folder / "output"

    if not desc.exists():
        continue

    inputs = sorted(inp.glob("input_*.txt"),
                    key=lambda p: int(p.stem.split("_")[1]))
    outputs = sorted(out.glob("output_*.txt"),
                     key=lambda p: int(p.stem.split("_")[1]))

    if len(inputs) != len(outputs):
        continue

    problems.append({
        "id": folder.name,
        "description": desc.read_text(encoding="utf-8"),
        "inputs": [p.read_text(encoding="utf-8") for p in inputs],
        "outputs": [p.read_text(encoding="utf-8") for p in outputs],
    })

print(f"Loaded problems: {len(problems)}")

# =========================================================
# Execution helpers
# =========================================================
def write_temp_py(code: str) -> str:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False)
    f.write(code)
    f.close()
    return f.name

def run_py(path: str, input_text: str, timeout=5.0):
    try:
        p = subprocess.run(
            [sys.executable, path],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return p.stdout, p.stderr, p.returncode, False
    except subprocess.TimeoutExpired:
        return "", "TIMEOUT", None, True

def normalize(s: str) -> str:
    lines = [ln.rstrip() for ln in s.splitlines()]
    while lines and lines[0] == "":
        lines.pop(0)
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)

def compare(exp: str, act: str) -> bool:
    e, a = normalize(exp), normalize(act)
    if e == a:
        return True
    try:
        return math.isclose(float(e), float(a), rel_tol=1e-6, abs_tol=1e-9)
    except:
        return False

# =========================================================
# MAIN LOOP
# =========================================================
START_INDEX = 0
NUM_PROBLEMS = 164

total_run = 0
total_passed = 0

for idx in range(START_INDEX, min(len(problems), START_INDEX + NUM_PROBLEMS)):
    prob = problems[idx]

    print("\n" + "=" * 80)
    print(f"[{idx+1}/{len(problems)}] Problem ID: {prob['id']}")
    print("=" * 80)

    code = generate_with_local_ollama(prob["description"])

    # 🔥 PRINT GENERATED CODE
    print("\n--- GENERATED CODE ---\n")
    print(code)
    print("\n--- END GENERATED CODE ---\n")

    path = write_temp_py(code)
    passed_all = True

    for i, (inp, exp) in enumerate(zip(prob["inputs"], prob["outputs"]), 1):
        out, err, rc, timeout = run_py(path, inp)
        ok = (not timeout) and rc == 0 and compare(exp, out)

        print(f"Test {i}: {'PASS' if ok else 'FAIL'}")

        if not ok:
            passed_all = False
            print("Expected:", repr(normalize(exp)))
            print("Got     :", repr(normalize(out)))
            print("Stderr  :", err)

    print("\nRESULT:", "✅ PASSED" if passed_all else "❌ FAILED")

    total_run += 1
    if passed_all:
        total_passed += 1

# =========================================================
# FINAL SUMMARY
# =========================================================
percent = (total_passed / total_run) * 100 if total_run else 0

print("\n" + "=" * 80)
print("FINAL RESULTS")
print("=" * 80)
print(f"Problems run     : {total_run}")
print(f"Problems passed  : {total_passed}")
print(f"Pass percentage  : {percent:.2f}%")

sys.stdout.close()
