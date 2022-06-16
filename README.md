# engine-similarity
Utility to compute evaluation correlation matrix for specified engines.

## Dependencies

`Python >= 3.8`

`python3 -m pip install numpy chess`

## Example Usage: 

To compute correlation coefficients, paths to compiled engine binaries, a path to a text file containing a list of fens and a desired search depth must all be specified.

```
$ python3 main.py --engine berserk --engine stockfish_12 --engine fire --depth 1 --fens fens.txt
corr(berserk, berserk) = 1.0
corr(berserk, stockfish_12) = 0.5356738825368556
corr(berserk, fire) = 0.562181605852763
corr(stockfish_12, berserk) = 0.5356738825368556
corr(stockfish_12, stockfish_12) = 0.9999999999999997
corr(stockfish_12, fire) = 0.9273272205303431
corr(fire, berserk) = 0.562181605852763
corr(fire, stockfish_12) = 0.9273272205303431
corr(fire, fire) = 1.0
```
