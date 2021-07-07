import sys
from pathlib import Path

sys.path.append(".")
for dir in set(path.parent for path in Path(".").glob("**/*.py")):
    sys.path.append(str(dir))