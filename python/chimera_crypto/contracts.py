from dataclasses import dataclass
from typing import Any
import json

@dataclass(frozen=True)
class InteropEnvelope:
    schema: str
    version: int
    operation: str
    payload: dict[str, Any]

    def to_json(self) -> str:
        return json.dumps({"schema": self.schema, "version": self.version, "operation": self.operation, "payload": self.payload}, sort_keys=True)

    @classmethod
    def from_json(cls, value: str) -> "InteropEnvelope":
        obj = json.loads(value)
        if obj.get("schema") != "chimera.crypto.interop" or obj.get("version") != 1:
            raise ValueError("unsupported interoperability envelope")
        return cls(obj["schema"], obj["version"], obj["operation"], obj["payload"])
