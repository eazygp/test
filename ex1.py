#!/usr/bin/env python3

import os
import sys
from collections import Counter

def get_shebang(filepath):
    try:
        with open(filepath, 'rb') as f:
            first_line = f.readline().decode('utf-8', errors='ignore').strip()
            if first_line.startswith('#!'):
                return first_line
    except Exception:
        pass
    return None

def conta_script(directory):
    counter = Counter()
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            if os.access(full_path, os.X_OK) and os.path.isfile(full_path):
                shebang = get_shebang(full_path)
                if shebang:
                    counter[shebang] += 1
    for shebang, count in counter.most_common():
        print(f"{count} {shebang}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: contaScript <directory>")
        sys.exit(1)
    conta_script(sys.argv[1])