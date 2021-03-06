#!/usr/bin/env python3

# Copyright 2012-2016 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess, sys, os
import shutil
from mesonbuild import mesonlib

if __name__ == '__main__':
    returncode = 0
    if mesonlib.is_linux():
        myenv = os.environ.copy()
        myenv['CC'] = 'gcc'
        myenv['CXX'] = 'g++'
        print('Running unittests with GCC.\n')
        returncode += subprocess.call([sys.executable, 'run_unittests.py', '-v'], env=myenv)
        if shutil.which('clang'):
            myenv['CC'] = 'clang'
            myenv['CXX'] = 'clang++'
            print('\nRunning unittests with clang.\n')
            returncode += subprocess.call([sys.executable, 'run_unittests.py', '-v'], env=myenv)
    returncode += subprocess.call([sys.executable, 'run_project_tests.py'] + sys.argv[1:])
    sys.exit(returncode)
