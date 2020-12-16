[![Python][python-test-image]][python-test-url]

[python-test-image]: https://github.com/dondakeshimo/tocot/workflows/Python%20poetry%20lint%20test%20build/badge.svg
[python-test-url]:   https://github.com/dondakeshimo/tocot/actions?query=workflow%3APython%20poetry%20lint%20test%20build

# tocot
Table Of Contents wO Tsukuru

This script build a TOC for markdown

# Required
Python >= 3.7

# Install
```
pip install tocot
```

# Usage
```
$ tocot --help
Usage: tocot [OPTIONS] IN_FILE OUT_FILE

Options:
  -l, --level INTEGER    [default: 2]
  -e, --to_embed TEXT    [default: [TOC]]
  --exclude_symbol TEXT  [default: exclude-toc]
  --help                 Show this message and exit.
```

### example
You have to write "[TOC]" in your markdown file, then run below command, "[TOC]" is replaced to Table of Contents.
```
$ tocot README.md new_README.md
```

If you want to change "[TOC]" to "table of contents template".
```
$ tocot -e "table of contents template" README.md new_README.md
```

You can select how deep include Table of contents.
Including title level is defined the number of "#".
```
$ tocot -l 4 README.md new_README.md
```

If you want to exclude title, you write comment "exclude-toc" next to the title.
```
$ tocot README.md new_README.md
```

You can change "exclude-toc" to "i hate this title".
```
$ tocot --exclude_symbol "i hate this title" README.md new_README.md
```

if you want to debug, you can write to stdout.
```
$ tocot README.md -
```
