from dataclasses import dataclass, field


@dataclass(frozen=True)
class User:
    id: str
    name: str
    age: int = field(repr=False) # Don't appear in repr
    friends: list = field(default_factory=list) # Empty list by default
    
    
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # Don't set in __init__
    
    def __post_init__(self):
        self.area = self.width * self.height