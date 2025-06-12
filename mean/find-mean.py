#!/usr/bin/env python3

import sys

def find_mean(path: str) -> float:
    count: int = 0
    total: float = 0.0

    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            columns = line.split(',')

            if len(columns) < 2:
                continue

            value = columns[1].strip().strip('"').strip("'")

            try:
                value = float(value)
                total += value
                count += 1

            except ValueError:
                continue
    return total / count if count > 0 else None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ..')
        sys.exit(1)
    ans = find_mean(sys.argv[1])
    print(ans)
