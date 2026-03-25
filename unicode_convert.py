import sys
import re

BOLD_MAP = {}

# Bold: Mathematical Sans-Serif Bold
bold_upper = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
bold_lower = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
bold_digits = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    BOLD_MAP[c] = bold_upper[i]
for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
    BOLD_MAP[c] = bold_lower[i]
for i, c in enumerate("0123456789"):
    BOLD_MAP[c] = bold_digits[i]

def to_bold(text):
    return "".join(BOLD_MAP.get(c, c) for c in text)

def has_boldable_chars(text):
    """英数字が含まれているか判定"""
    return any(c in BOLD_MAP for c in text)

def to_bold_mixed(text):
    """英数字をUnicode太字に変換、日本語はそのまま"""
    return "".join(BOLD_MAP.get(c, c) for c in text)

def bold_replace_inline(m):
    """インライン太字の置換: 英数字→Unicode太字、日本語のみ→「」で囲む"""
    inner = m.group(1)
    if has_boldable_chars(inner):
        return to_bold_mixed(inner)
    else:
        # 日本語のみの太字 → 「」で強調
        return "「" + inner + "」"

def process_article(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        line = line.rstrip("\n")

        # 見出し行: 太字にする
        if line.startswith("## "):
            text = line[3:]
            result.append("\n" + to_bold_mixed(text) + "\n")
        elif line.startswith("# ") and not line.startswith("# X"):
            text = line[2:]
            result.append(to_bold_mixed(text) + "\n")
        elif line.startswith("# X") or line.startswith("==="):
            continue  # skip meta lines
        elif line.startswith("**") and line.endswith("**"):
            # Full bold line
            text = line.strip("*")
            if has_boldable_chars(text):
                result.append(to_bold_mixed(text))
            else:
                result.append("「" + text + "」")
        else:
            # Inline bold: **text**
            processed = re.sub(r'\*\*(.+?)\*\*', bold_replace_inline, line)
            result.append(processed)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(result))

    print(f"変換完了: {output_path}")

if __name__ == "__main__":
    import os
    # コマンドライン引数があればそれを使う、なければデフォルト
    if len(sys.argv) >= 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "x_article_for_convert.md"
        output_file = "x_article_ready.txt"
    process_article(input_file, output_file)
