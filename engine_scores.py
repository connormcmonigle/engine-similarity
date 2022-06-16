from dataclasses import dataclass
import numpy as np
import numpy.typing as npt


@dataclass
class EngineScores:
  name: str
  scores: npt.NDArray[np.float32]

  @staticmethod
  def correlation(a: "EngineScores", b: "EngineScores") -> float:
    a_values = a.scores - a.scores.mean()
    b_values = b.scores - b.scores.mean()
    return np.dot(a_values, b_values) / np.sqrt((a_values * a_values).sum() * (b_values * b_values).sum())
