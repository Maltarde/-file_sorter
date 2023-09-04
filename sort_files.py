from pathlib import Path
import sys

EXTENSIONS_MAPPING = {".mp3": "Musique",
                      ".wav": "Musique",
                      ".mp4": "Videos",
                      ".avi": "Videos",
                      ".bmp": "Images",
                      ".png": "Images",
                      ".jpg": "Images",
                      ".txt": "Documents",
                      ".pptx": "Documents",
                      ".xls": "Documents",
                      ".odp": "Documents",}


if len(sys.argv) <= 1:
    BASE_DIR = Path().cwd()
else:
    BASE_DIR = Path(sys.argv[1])

files = [f for f in BASE_DIR.iterdir() if f.is_file()]
for file in files:  # On boucle sur chaque fichier
    target_folder = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    absolute_target_folder = BASE_DIR / target_folder 
    absolute_target_folder.mkdir(exist_ok=True)
    target_file  = absolute_target_folder / file.name
    file.rename(target_file)
