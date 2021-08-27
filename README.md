# HelltakerSolver
## Installation
Clone Repo, open console and navigate to repo:
```
// If you want, setup a python environment using your preferred tool
python -m venv .env
.env/scripts/activate

// Install the local package
pip install .
```

## Basic Usage
HelltakerSolver only features a simple Brute Force algorithm. It can be used via commandline and requires a json file which describes the map. See the <a href="https://github.com/AdamantLife/Helltaker">Helltaker module</a> (which servers as the basis for the module) for information on how to format the json file.

Commandline:

```
HelltakerSolver BruteForce [pathtojson]
```

The Solver will output all valid solutions it discovered. For each it will list the remaining Willpower for the path and the list of directional inputs required to complete the map along the path.