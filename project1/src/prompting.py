from pathlib import Path

def load_template(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")

def render_mcq(template: str, question: str, choices: list[str]) -> str:
    assert len(choices) == 4
    return template.format(
        question=question,
        A=choices[0], B=choices[1], C=choices[2], D=choices[3]
    )