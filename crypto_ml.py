"""Optional CNN/RNN deep-learning research models.

PyTorch is optional.  Models operate on public numerical research data only;
they do not infer or recover private keys.
"""
from __future__ import annotations

try:
    import torch
    from torch import nn
except ImportError:  # pragma: no cover
    torch = None
    nn = None


def _require_torch():
    if torch is None:
        raise RuntimeError("Install optional ML dependencies with: pip install -r requirements-ml.txt")


class CryptoCNN(nn.Module if nn else object):
    def __init__(self, channels: int = 4, classes: int = 2):
        _require_torch()
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv1d(channels, 32, 3, padding=1), nn.ReLU(),
            nn.Conv1d(32, 64, 3, padding=1), nn.ReLU(),
            nn.AdaptiveAvgPool1d(1), nn.Flatten(), nn.Linear(64, classes)
        )

    def forward(self, x):
        return self.net(x)


class CryptoRNN(nn.Module if nn else object):
    def __init__(self, features: int = 4, hidden: int = 64, classes: int = 2):
        _require_torch()
        super().__init__()
        self.rnn = nn.GRU(features, hidden, batch_first=True)
        self.head = nn.Linear(hidden, classes)

    def forward(self, x):
        output, _ = self.rnn(x)
        return self.head(output[:, -1, :])


def train_classifier(model, x, y, epochs: int = 5, lr: float = 1e-3):
    _require_torch()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    history = []
    for _ in range(epochs):
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
        history.append(float(loss.detach().cpu()))
    return history
