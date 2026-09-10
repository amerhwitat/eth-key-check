import { randomUUID } from 'node:crypto';

export function auditEvent(event, component, detail) {
  return { id: randomUUID(), event, component, detail, timestamp: new Date().toISOString() };
}
