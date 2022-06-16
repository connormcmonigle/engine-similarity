from engine_scores import EngineScores
from engine_scores_builder import EngineScoresBuilder

from typing import List
import chess.engine
import asyncio
import argparse
import os


async def main():
  parser = argparse.ArgumentParser(description="Compute engine similarity.")
  parser.add_argument("--engine", action="append", required=True, type=str)
  parser.add_argument("--fens", required=True, type=str)
  parser.add_argument("--depth", required=True, type=int)
  args = parser.parse_args()

  engine_names_and_paths = [(str(engine), os.path.join(os.getcwd(), str(engine))) for engine in args.engine]
  engine_score_data: List[EngineScores] = []

  for name, engine_path in engine_names_and_paths:
    data = await EngineScoresBuilder(depth_limit=args.depth, fens_path=args.fens).build(name, engine_path)
    engine_score_data.append(data)

  for a in engine_score_data:
    for b in engine_score_data:
      correlation = EngineScores.correlation(a, b)
      print(f"corr({a.name}, {b.name}) = {correlation}")

if __name__ == "__main__":
  asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
  asyncio.run(main())