#!/usr/bin/python3

import matlab.engine
import sys
import os.path


cwd = os.getcwd()
file = sys.argv[1]
fullpath = os.path.join(cwd, file)
dirpath = os.path.dirname(fullpath)
basename = os.path.basename(fullpath)

# connect to engine and cd to working directory

try:
    eng = matlab.engine.connect_matlab('matex')
    eng.cd(dirpath)
except matlab.engine.EngineError as e:
    print(f'{e}', file=sys.stderr)
    exit(1)
except matlab.engine.MatlabExecutionError as e:
    exit(1)

# run cript

try:
    eng.__getattr__(basename.rstrip('.m'))(nargout=0)
except matlab.engine.MatlabExecutionError:
    exit(1)

