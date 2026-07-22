import shutil
from pathlib import Path

def clear_destination(destination_root: Path) -> None:
    if destination_root == Path(".") or destination_root == Path("/"):
        raise ValueError("Don't delete this please")
    
    if destination_root.exists():
        shutil.rmtree(destination_root)
        print(f"Cleared: {destination_root}")

    destination_root.mkdir(parents=True)
    print(f"Created empty: {destination_root}")

def copy_item(source: Path, destination_root: Path, relative_to: Path) -> None:
    relative_path = source.relative_to(relative_to)
    target = destination_root / relative_path

    if source.is_dir():
        target.mkdir(parents=True, exist_ok=True)
        print(f"Created dir:  {target}")
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        print(f"Copied file:  {source} -> {target}")


def scan_folder(source: Path, destination_root: Path, relative_to: Path | None = None) -> None:
    if relative_to is None:
        relative_to = source

    for entry in source.iterdir():
        copy_item(entry, destination_root, relative_to)

        if entry.is_dir():
            scan_folder(entry, destination_root, relative_to)


if __name__ == "__main__":
    source = Path("source_folder")
    destination = Path("destination_folder")

    clear_destination(destination)
    scan_folder(source, destination)