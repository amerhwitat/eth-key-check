"""Optional Gymnasium/Stable-Baselines3 research environment.

This is a paper/backtesting environment. It does not connect to an exchange,
place orders, or move funds.
"""
from __future__ import annotations

import numpy as np

try:
    import gymnasium as gym
    from gymnasium import spaces
except ImportError:  # pragma: no cover
    gym = None
    spaces = None


class CryptoResearchEnv(gym.Env if gym else object):
    """Long-only toy environment over an offline feature matrix.

    Actions: 0=hold, 1=allocate, 2=reduce.
    Observations are normalized public market/research features.
    """
    metadata = {"render_modes": []}

    def __init__(self, features, returns):
        if gym is None:
            raise RuntimeError("Install optional RL dependencies with: pip install -r requirements-ml.txt")
        self.features = np.asarray(features, dtype=np.float32)
        self.returns = np.asarray(returns, dtype=np.float32)
        if len(self.features) != len(self.returns) or len(self.features) < 2:
            raise ValueError("features and returns must have equal length >= 2")
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(-np.inf, np.inf,
                                            shape=self.features.shape[1:], dtype=np.float32)
        self.index = 0
        self.position = 0.0

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        self.index, self.position = 0, 0.0
        return self.features[self.index], {}

    def step(self, action):
        if action == 1:
            self.position = min(1.0, self.position + 0.25)
        elif action == 2:
            self.position = max(0.0, self.position - 0.25)
        reward = float(self.position * self.returns[self.index])
        self.index += 1
        terminated = self.index >= len(self.features) - 1
        return self.features[self.index], reward, terminated, False, {"position": self.position}


def train_ppo(env, total_timesteps=10_000, seed=7):
    try:
        from stable_baselines3 import PPO
    except ImportError as exc:
        raise RuntimeError("Install optional RL dependencies with: pip install -r requirements-ml.txt") from exc
    model = PPO("MlpPolicy", env, verbose=0, seed=seed)
    model.learn(total_timesteps=total_timesteps)
    return model
