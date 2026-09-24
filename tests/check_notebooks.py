"""檢查教材格式：不用執行 notebook，幾秒內完成。

    python tests/check_notebooks.py            # 檢查格式與敏感資訊
    python tests/check_notebooks.py --executed # 另外檢查每一格都有執行、沒有錯誤輸出（發布前使用）
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import nbformat

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = REPO_ROOT / 'notebooks'

NO_LOGIN_NOTEBOOKS = {'ch1_u03_taiex_kbar_crawler.ipynb'}  # 爬蟲練習只用 requests，不需要登入
SETUP_LINES = ('finlab.login()', 'data.set_storage(data.FileStorage())')
HEADER_KEYWORDS = ('**對應影片**', '**和影片的差異**')
PARAMETERS_TAG = 'parameters'

FORBIDDEN_PATTERNS = {
    'shift': re.compile(r'\bshift\b', re.IGNORECASE),
    '本機路徑': re.compile(r'/Users/|/home/[a-z]|/private/var|/var/folders/|[A-Za-z]:\\\\Users\\\\'),
    'email': re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+'),
    'token': re.compile(r'FINLAB_(API_TOKEN|REFRESH_TOKEN|SESSION_ID|API_KEY)\s*=\s*\S+'),
}


def check(path: Path, executed: bool) -> list[str]:
    notebook = nbformat.read(path, as_version=4)
    cells = notebook.cells
    problems = []

    first = cells[0]
    if first.cell_type != 'code':
        problems.append('第一格必須是程式碼（安裝與登入）')
    elif path.name not in NO_LOGIN_NOTEBOOKS and not all(line in first.source for line in SETUP_LINES):
        problems.append(f'第一格必須包含 {SETUP_LINES}')

    header = next((cell for cell in cells if cell.cell_type == 'markdown'), None)
    if header is None or not all(keyword in header.source for keyword in HEADER_KEYWORDS):
        problems.append(f'第一個說明格必須包含 {HEADER_KEYWORDS}')

    for cell in cells:
        if PARAMETERS_TAG in cell.metadata.get('tags', []) and 'QUICK_RUN = False' not in cell.source:
            problems.append('parameters 格的預設值必須是 QUICK_RUN = False')

    sources = '\n'.join(cell.source for cell in cells)
    if FORBIDDEN_PATTERNS['shift'].search(sources):
        problems.append('教材中不應出現 shift')

    raw = json.dumps(notebook, ensure_ascii=False)
    for name in ('本機路徑', 'email', 'token'):
        if match := FORBIDDEN_PATTERNS[name].search(raw):
            problems.append(f'含有{name}：{match.group(0)[:40]}')

    if executed:
        code_cells = [cell for cell in cells if cell.cell_type == 'code']
        if any(cell.execution_count is None for cell in code_cells):
            problems.append('有程式格沒有執行')
        if any(output.output_type == 'error' for cell in code_cells for output in cell.outputs):
            problems.append('有程式格的輸出是錯誤')
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--executed', action='store_true', help='檢查輸出是否完整')
    args = parser.parse_args()

    failed = False
    for path in sorted(NOTEBOOK_DIR.glob('*.ipynb')):
        problems = check(path, args.executed)
        failed |= bool(problems)
        print(f'{"FAIL" if problems else "OK  "}  {path.name}')
        for problem in problems:
            print(f'      - {problem}')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
