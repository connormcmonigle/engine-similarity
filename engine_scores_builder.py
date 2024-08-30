from engine_scores import EngineScores

from dataclasses import dataclass
import chess
import chess.engine
import numpy as np

@dataclass
class EngineScoresBuilder:
  depth_limit: int
  fens_path: str

  async def build(self, name: str, engine_path: str) -> EngineScores:
    SCORE = "score"
    MATE_SCORE = 100_000

    _, engine = await chess.engine.popen_uci(engine_path)
    with open(self.fens_path) as fens_file:
      fens = fens_file.readlines()
    
    scores = []
    for board in [chess.Board(fen) for fen in fens]:
      result = await engine.play(board, chess.engine.Limit(depth = self.depth_limit), info=chess.engine.Info.SCORE)
      scores.append(result.info[SCORE].relative)

    await engine.quit()
    return EngineScores(name=name, scores=np.array([float(score.score(mate_score=MATE_SCORE)) for score in scores]))
