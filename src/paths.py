"""Project paths, so notebooks can find data regardless of where they live.

Usage in a notebook:

    import sys; sys.path.append("..")     # if the notebook is in notebooks/
    from src.paths import RAW, PROCESSED

    df = pd.read_csv(RAW / "housing.csv")
"""

from pathlib import Path

# This file is at <project>/src/paths.py, so the project root is two levels up.
ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"
EXTERNAL = DATA / "external"
MODELS = ROOT / "models"

__all__ = ["ROOT", "DATA", "RAW", "PROCESSED", "EXTERNAL", "MODELS"]
