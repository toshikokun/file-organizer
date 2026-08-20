from pathlib import Path
import shutil

dir_path=Path('/Users/toshikokun/Desktop/file_organizer:')

categories={
    ".jpg":"画像",
    ".png":"画像",
    ".pdf":"PDF",
    ".csv":"CSV",
    ".txt":"テキスト"
}

for entry in dir_path.iterdir():
    if not entry.is_file():
        continue

    category=categories.get(entry.suffix)
    no_path=dir_path/"その他"
    if category is None:
        category="その他"
    path= dir_path / category
    path.mkdir(exist_ok=True)
    print(f"{entry} → {category}")
    destination=path/entry.name
    shutil.move(entry,destination)

