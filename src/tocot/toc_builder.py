import typing


class TOCBuilder:
    def __init__(self, in_file: typing.TextIO, out_file: typing.TextIO,
                 level: int) -> None:
        self.in_file = in_file
        self.out_file = out_file
        self.level = level
        self.section_counter = [0] * self.level
        self.toc = ""
        self.new_contents = ""

    def build(self) -> None:
        for line in self.in_file:
            if not self._is_header(line):
                continue

            self._insert_section(line)

    def write(self) -> None:
        pass

    def _insert_section(self, line: str) -> None:
        pass

    def _is_header(self, line: str) -> bool:
        pass

    def _detect_level(self, line: str) -> int:
        pass

    def _append_toc_row(self) -> None:
        pass
