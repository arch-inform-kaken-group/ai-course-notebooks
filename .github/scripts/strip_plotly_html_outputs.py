import json
import shutil
from pathlib import Path


SRC_DIR = Path("notebooks")
BUILD_DIR = Path("notebooks_build")


PLOTLY_MARKERS = [
    "Plotly.newPlot",
    "plotly-graph-div",
    "cdn.plot.ly",
    "window.PlotlyConfig",
]


PLOTLY_MIME_KEYS = [
    "text/html",
    "application/vnd.plotly.v1+json",
    "application/javascript",
]


def as_text(value) -> str:
    if isinstance(value, list):
        return "".join(str(v) for v in value)
    return str(value)


def is_plotly_html(value) -> bool:
    text = as_text(value)
    return any(marker in text for marker in PLOTLY_MARKERS)


def strip_plotly_outputs_from_notebook(path: Path) -> int:
    nb = json.loads(path.read_text(encoding="utf-8"))
    changed = 0

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue

        new_outputs = []

        for output in cell.get("outputs", []):
            data = output.get("data")

            if not isinstance(data, dict):
                new_outputs.append(output)
                continue

            remove_keys = []

            for key in PLOTLY_MIME_KEYS:
                if key not in data:
                    continue

                if key == "text/html":
                    if is_plotly_html(data[key]):
                        remove_keys.append(key)
                else:
                    
                    remove_keys.append(key)

            if remove_keys:
                for key in remove_keys:
                    data.pop(key, None)
                changed += 1

            
            if output.get("output_type") in {"display_data", "execute_result"} and not data:
                continue

            new_outputs.append(output)

        cell["outputs"] = new_outputs

    if changed:
        path.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1),
            encoding="utf-8",
        )

    return changed


def main() -> None:
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)

    shutil.copytree(SRC_DIR, BUILD_DIR)

    total = 0

    for path in BUILD_DIR.rglob("*.ipynb"):
        changed = strip_plotly_outputs_from_notebook(path)
        if changed:
            print(f"{path}: stripped {changed} Plotly output bundle(s)")
            total += changed

    print(f"Total stripped Plotly output bundle(s): {total}")


if __name__ == "__main__":
    main()
