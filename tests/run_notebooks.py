"""從頭到尾執行 notebooks，任何一格出錯就回報失敗。

用法：
    python tests/run_notebooks.py                     # 執行全部，結果寫到 build/executed/
    python tests/run_notebooks.py --quick             # QUICK_RUN=True：縮小 epoch 與樣本，用來快速檢查
    python tests/run_notebooks.py --inplace           # 把執行結果寫回 notebooks/（更新教材內保存的輸出）
    python tests/run_notebooks.py notebooks/ch2_*.ipynb
"""

from __future__ import annotations

import argparse
import sys
import tempfile
import time
from pathlib import Path

import nbformat
import papermill

from sanitize import sanitize

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = REPO_ROOT / 'notebooks'
DEFAULT_OUTPUT_DIR = REPO_ROOT / 'build' / 'executed'
PARAMETERS_TAG = 'parameters'
CELL_TIMEOUT_SECONDS = 3600


def has_parameters_cell(path: Path) -> bool:
    notebook = nbformat.read(path, as_version=4)
    return any(PARAMETERS_TAG in cell.metadata.get('tags', []) for cell in notebook.cells)


def execute(path: Path, output: Path, quick: bool) -> None:
    parameters = {'QUICK_RUN': True} if quick and has_parameters_cell(path) else {}
    with tempfile.TemporaryDirectory() as workdir:
        papermill.execute_notebook(
            str(path),
            str(output),
            parameters=parameters,
            cwd=workdir,
            kernel_name='python3',
            execution_timeout=CELL_TIMEOUT_SECONDS,
            progress_bar=False,
        )
    notebook = nbformat.read(output, as_version=4)
    nbformat.write(sanitize(notebook), output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('notebooks', nargs='*', type=Path, help='要執行的 notebook，預設為 notebooks/ 全部')
    parser.add_argument('--quick', action='store_true', help='以 QUICK_RUN=True 執行')
    parser.add_argument('--inplace', action='store_true', help='把輸出寫回原本的 notebook')
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    paths = sorted(args.notebooks) or sorted(NOTEBOOK_DIR.glob('*.ipynb'))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    failures = []
    for path in paths:
        output = path if args.inplace else args.output_dir / path.name
        started = time.monotonic()
        try:
            execute(path, output, args.quick)
        except Exception as error:  # 任何錯誤都要記錄下來，繼續跑下一本
            failures.append(path.name)
            print(f'FAIL  {path.name}  ({time.monotonic() - started:.0f}s)\n      {error}'.rstrip(), flush=True)
            continue
        print(f'PASS  {path.name}  ({time.monotonic() - started:.0f}s)', flush=True)

    print(f'\n{len(paths) - len(failures)}/{len(paths)} notebooks passed')
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
