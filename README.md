# file-template

┌────────────────────────────────────────────────────┐
│░█▀▀░▀█▀░█░░░█▀▀░░░░░▀█▀░█▀▀░█▄█░█▀█░█░░░█▀█░▀█▀░█▀▀│
│░█▀▀░░█░░█░░░█▀▀░▄▄▄░░█░░█▀▀░█░█░█▀▀░█░░░█▀█░░█░░█▀▀│
│░▀░░░▀▀▀░▀▀▀░▀▀▀░░░░░░▀░░▀▀▀░▀░▀░▀░░░▀▀▀░▀░▀░░▀░░▀▀▀│
└────────────────────────────────────────────────────┘

Replaces keywords in a file with the contents of another file

# Installation

```
pipx install file-template
```

# CLI Usage

```
Usage: file-template [OPTIONS] KEYWORD FILE1 FILE2

  Replace KEYWORD in FILE1 with the contents of FILE2.

Options:
  -i, --inplace   Edit the file in place instead of outputting to stdout.
  -n, --no-strip  Do not strip FILE2 of leading or trailing blank characters.
  --help          Show this message and exit.
```

# Author

* Alexandre Janvrin, penetration tester at Beijaflore (https://www.beijaflore.com/en/)

# License

AGPLv3+, see LICENSE.txt for more details.

# URLs

* https://pypi.org/project/file-template/
* https://github.com/LivinParadoX/file-template/
