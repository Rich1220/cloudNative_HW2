import subprocess
import re
from pathlib import Path

def test_cli_output_matches_expected():
    print("✅ 測試函數真的有執行到嗎？")

    project_dir = Path(__file__).resolve().parent.parent
    run_script = project_dir / "run.sh"
    input_file = project_dir / "test/input.txt"
    expected_file = project_dir / "test/expected_output.txt"

    # 執行 run.sh，把 input.txt 丟給它
    with open(input_file, "r") as fin:
        result = subprocess.run(
            [str(run_script)],
            stdin=fin,
            capture_output=True,
            text=True
        )

    # 拆行
    output_lines = result.stdout.strip().splitlines()
    with open(expected_file, "r") as fexp:
        expected_lines = fexp.read().strip().splitlines()

    # 比對每一行
    for i, (actual, expected) in enumerate(zip(output_lines, expected_lines)):
        if "[TIME]" in expected:
            # 把 [TIME] 替換成 datetime 格式的 regex
            pattern = re.escape(expected).replace(r"\[TIME\]", r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
            assert re.fullmatch(pattern, actual), f"[Line {i+1}] 時間格式不符：\n  actual:   {actual}\n  expected: {expected}"
        else:
            assert actual == expected, f"[Line {i+1}] 不一致：\n  actual:   {actual}\n  expected: {expected}"
