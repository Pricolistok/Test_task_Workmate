from dataclasses import dataclass, field


@dataclass
class SpentStat:
    spent: list[int] = field(default_factory=list)
    median: float = 0