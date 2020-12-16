import unittest
import pathlib

from tocot.toc_builder import TOCBuilder


class TestTOCBuilder(unittest.TestCase):
    def test_build(self):
        """ test build method """
        testdata_dir = pathlib.Path("tests/testdata")
        testmd = testdata_dir / "test.md"

        tests = [
            {
                "want_file": "want_no_option.md",
                "level": 2,
                "to_embed": "[TOC]",
                "exclude_symbol": "exclude-toc",
            },
            {
                "want_file": "want_level1.md",
                "level": 1,
                "to_embed": "[TOC]",
                "exclude_symbol": "exclude-toc",
            },
            {
                "want_file": "want_level3.md",
                "level": 3,
                "to_embed": "[TOC]",
                "exclude_symbol": "exclude-toc",
            },
            {
                "want_file": "want_level4.md",
                "level": 4,
                "to_embed": "[TOC]",
                "exclude_symbol": "exclude-toc",
            },
            {
                "want_file": "want_level5.md",
                "level": 5,
                "to_embed": "[TOC]",
                "exclude_symbol": "exclude-toc",
            },
            {
                "want_file": "want_to_embed.md",
                "level": 4,
                "to_embed": "{TOC-other}",
                "exclude_symbol": "exclude-toc",
            },
        ]

        for tt in tests:
            in_file = open(str(testmd), "r")
            builder = TOCBuilder(in_file, None, tt["level"], tt["to_embed"],
                                 tt["exclude_symbol"])
            builder.build()

            with open(str(testdata_dir / tt["want_file"]), "r") as f:
                want = f.read()
                self.assertEqual(builder.new_contents, want)

            in_file.close()
