from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class MessageTemplate:
    id: str
    title: str
    body: str
    variables: list[str] = field(default_factory=list)
