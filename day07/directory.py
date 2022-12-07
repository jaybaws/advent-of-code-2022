from __future__ import annotations
from dataclasses import dataclass, field
from file import File

@dataclass()
class Directory:
    name: str = field(compare=True)
    parent: Directory = None
    subdirs: set[Directory] = field(default_factory=set, repr=False, compare=False)
    files: set[File] = field(default_factory=set, repr=False, compare=False)


    def total_size(self) -> int:
        return sum(int(file.file_size()) for file in self.files) + sum(int(subdir.total_size()) for subdir in self.subdirs)

    def addFile(self, f: File) -> None:
        self.files.add(f)

    def addDir(self, d: Directory) -> None:
        self.subdirs.add(d)

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        if self.parent is None:
            return ""
        else:
            return self.parent.__repr__() + '/' + self.name