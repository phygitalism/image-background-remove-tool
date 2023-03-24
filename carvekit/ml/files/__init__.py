from pathlib import Path
import os

carvekit_dir = Path(os.environ.get(
    "CARVEKIT_HOME",  Path.home().joinpath(".cache/carvekit")))

carvekit_dir.mkdir(parents=True, exist_ok=True)

checkpoints_dir = carvekit_dir.joinpath("checkpoints")
