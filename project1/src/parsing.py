import re

def parse_choice_letter(text: str) -> str | None:
    # 目标：只认 A/B/C/D。其余都算解析失败，方便统计失败率
    m = re.search(r"\b([ABCD])\b", text.strip().upper())
    return m.group(1) if m else None