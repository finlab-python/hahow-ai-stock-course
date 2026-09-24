"""清理執行後的 notebook：移除執行環境資訊，只留下學生需要看的輸出。"""

from __future__ import annotations

import re

import nbformat

LOCAL_PATH = re.compile(r'(/Users/|/home/|/private/|/tmp/|/var/folders/|[A-Za-z]:\\Users\\)[^\s\'"<>]*')
PATH_PLACEHOLDER = '<local-path>'
EXECUTION_METADATA_KEYS = ('papermill', 'execution')
CLEAR_OUTPUT_TAG = 'clear-output'  # 輸出太大（例如互動報表）的格子，不保存輸出


def _scrub(text: str) -> str:
    return LOCAL_PATH.sub(PATH_PLACEHOLDER, text)


def _clean_output(output: nbformat.NotebookNode) -> nbformat.NotebookNode | None:
    """stderr 多半是套件的警告與進度條，對學生沒有幫助，直接移除。"""
    if output.output_type == 'stream':
        if output.name == 'stderr':
            return None
        output.text = _scrub(output.text)
    elif output.output_type in ('display_data', 'execute_result'):
        for mime, content in output.data.items():
            if mime.startswith('text/') and isinstance(content, str):
                output.data[mime] = _scrub(content)
    return output


def sanitize(notebook: nbformat.NotebookNode) -> nbformat.NotebookNode:
    for key in EXECUTION_METADATA_KEYS:
        notebook.metadata.pop(key, None)
    for cell in notebook.cells:
        for key in EXECUTION_METADATA_KEYS:
            cell.metadata.pop(key, None)
        if cell.cell_type != 'code':
            continue
        if CLEAR_OUTPUT_TAG in cell.metadata.get('tags', []):
            cell.outputs = []
        else:
            cleaned = (_clean_output(output) for output in cell.outputs)
            cell.outputs = [output for output in cleaned if output is not None]
    return notebook
