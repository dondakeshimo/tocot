import typing


class TOCBuilder:
    HEADER_CHAR = "#"
    ITEM_CHAR = "* "
    ITEM_INDENT = "  "
    SECTION_JOINT = "-"
    SECTION_PREFIX = "sec"

    def __init__(self, in_file: typing.TextIO, out_file: typing.TextIO,
                 level: int) -> None:
        self.in_file = in_file
        self.out_file = out_file
        self.upper_level = level
        self.section_counter_list = [0] * self.upper_level
        self.toc_item_list = []
        self.new_contents_list = []
        self.toc = ""
        self.new_contents = ""

    def build(self) -> None:
        for line in self.in_file:
            if not self._is_header(line):
                self.new_contents_list.append(line)
                continue

            level = self._detect_level(line)
            if level > self.upper_level:
                self.new_contents_list.append(line)
                continue

            section = self._build_section(level)
            title = self._extract_header_title(line, level)

            self.new_contents_list.append(self._make_section_tag(section))
            self.new_contents_list.append(line)

            self._append_toc_row(title, section, level)

        self.toc = "\n".join(self.toc_item_list)
        self.new_contents = "".join(self.new_contents_list)

        # TODO: be able to chose place to insert TOC
        self.new_contents = self.toc + "\n\n" + self.new_contents

    def write(self) -> None:
        self.out_file.write(self.new_contents)

    def _is_header(self, line: str) -> bool:
        return line.startswith(self.HEADER_CHAR)

    def _detect_level(self, line: str) -> int:
        level = 0
        for char in line:
            if char != self.HEADER_CHAR:
                break
            level += 1

        return level

    def _append_toc_row(self, title: str, section: str, level: int) -> None:
        indent = self.ITEM_INDENT * (level - 1)
        title = f"[{title}]"
        section = f"(#{section})"
        self.toc_item_list.append(indent + self.ITEM_CHAR + title + section)

    def _extract_header_title(self, line: str, level: int) -> str:
        title = line[level:]
        return title.strip()

    def _build_section(self, level: int) -> str:
        for i in range(len(self.section_counter_list)):
            if i < level - 1:
                continue
            elif i == level - 1:
                self.section_counter_list[i] += 1
            else:
                self.section_counter_list[i] = 0

        section_num = [str(s) for s in self.section_counter_list]

        return self.SECTION_PREFIX + self.SECTION_JOINT.join(section_num)

    def _make_section_tag(self, section: str) -> str:
        return f"<a id=\"{section}\"></a>\n"
