from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class MessageTemplate:
    id: int
    title: str
    body: str
    variables: list[str] = field(default_factory=list)
