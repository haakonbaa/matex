# matex

Matlab script executioner and workspace viewer. Makes it easy to write matlab scripts without using the matlab GUI.

## Usage
```txt
USAGE:
    matex [ -w | -i | filename ]
  
OPTIONS:
    filename            Path to matlab file to execute
    -w | --workspace    Show workspace in terminal
    -i | --interactive  Open interactive terminal
```

## Example
Start the engine and interactive terminal by running
```bash
matex --interactive # -i
```
Now show all variables in workspace with
```bash
matex --workspace # -w
```
The variables are automatically refreshed about every 0.5 second. Execute a script by running
```bash
matex ./path/to/my_script.m
```

## Requirements
The code is tested with matlab R2022b, but it might work on any version >= R2014b.

This package uses mathwork's [matlab-engine-for-python](https://github.com/mathworks/matlab-engine-for-python) to connect to matlab. Install the package with:
```shell
python -m pip install matlabengine
```