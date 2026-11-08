"""Validate that a proposed publication ZIP contains no Git history."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import PurePosixPath


def check(path):
    """Fail for unsafe, duplicated or Git-bearing archive entries."""
    with zipfile.ZipFile(path, 'r') as z:
        infos = z.infolist()
        names = [i.filename for i in infos]
        assert len(names) == len(set(names)), 'Duplicate ZIP path'
        assert 'README.md' in names, 'ZIP must be rooted at the publication root'
        for info in infos:
            name = info.filename
            p = PurePosixPath(name)
            assert not name.startswith('/') and '\\' not in name, name
            assert not any(part in ('..', '.git') for part in p.parts), name
            assert not any(part in ('.env', '.venv') for part in p.parts), name
            assert not p.is_absolute(), name
            assert (info.external_attr >> 16) & 0o170000 != 0o120000, (
                'Symlink forbidden', name
            )
        bad = z.testzip()
        assert bad is None, ('Bad ZIP CRC', bad)
    print(f'History-free publication archive verified: {len(names)} files')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('archive')
    args = parser.parse_args()
    check(args.archive)
