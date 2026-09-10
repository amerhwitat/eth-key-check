from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json

@dataclass(frozen=True)
class AuditEvent:
    event: str
    component: str
    detail: str
    timestamp: str

    @classmethod
    def now(cls, event: str, component: str, detail: str) -> "AuditEvent":
        return cls(event, component, detail, datetime.now(timezone.utc).isoformat())

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)
