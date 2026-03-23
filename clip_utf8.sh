#!/bin/bash
# clip_utf8.sh - UTF-8テキストをWindowsクリップボードにコピー
# Usage: ./clip_utf8.sh <file>
# Usage: echo "text" | ./clip_utf8.sh
#
# Windows の clip.exe は UTF-8 非対応で文字化けするため、
# PowerShell の Set-Clipboard を経由して確実にUTF-8でコピーする

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -n "$1" ] && [ -f "$1" ]; then
    # ファイル指定
    powershell.exe -ExecutionPolicy Bypass -File "$SCRIPT_DIR/clip_utf8.ps1" -File "$1"
else
    # stdin から読み取り → 一時ファイル経由でコピー
    TMPFILE=$(mktemp /tmp/clip_utf8_XXXXXX.txt)
    cat > "$TMPFILE"
    powershell.exe -ExecutionPolicy Bypass -File "$SCRIPT_DIR/clip_utf8.ps1" -File "$TMPFILE"
    rm -f "$TMPFILE"
fi
