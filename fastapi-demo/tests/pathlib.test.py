import os
from pathlib2 import Path

print("## os ......")
print(os.path.dirname(os.getcwd()))
print("")
print("## Path ......")
print(Path.cwd().parent)

Path("test.txt").write_text("Hello, world!")
Path("test2.txt").touch(exist_ok=True)
Path("test2").mkdir(parents=True, exist_ok=True)
