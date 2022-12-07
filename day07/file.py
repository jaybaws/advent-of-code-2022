from dataclasses import dataclass, field

@dataclass
class File:
    name: str = field(compare=True)
    size: int = field(compare=False)

    def __hash__(self):
        return hash(self.name)

    def file_size(self) -> int:
        return self.size