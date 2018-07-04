#! /usr/bin/python3
try:
    import skbuild
    import PySide2
except ImportError:
    print("")
    print("***********************************************************************************")
    print("")
    print("skbuild or PySide2 not found, please execute:")
    print("pip3 install scikit-build")
    print("pip3 install --index-url=http://download.qt.io/snapshots/ci/pyside/5.11/latest/ pyside2 --trusted-host download.qt.io")
    print("")
    print("***********************************************************************************")
    print("")

from skbuild import setup
from setuptools import find_packages
import os

icons = [ "src/icons/" + filename for filename in os.listdir("src/icons")]
shaders = [ "src/shader/" + filename for filename in os.listdir("src/shader")]

CMAKE_ARGS = []

try:
    import netgen.NgOCC
    CMAKE_ARGS.append("-DUSE_OCC=ON")
except ImportError:
    pass

modules = ['ngsgui'] + ['ngsgui.' + pkg for pkg in find_packages('src')]
dirs = { module : module.replace('ngsgui.','src/') if 'ngsgui.' in module else 'src' for module in modules}

setup(name="ngsgui",
      version="0.1.4",
      description="New graphical interface for NGSolve",
      packages=modules,
      package_dir=dirs,
      data_files = [('share/ngsgui/icons', icons),
                    ('share/ngsgui/shader', shaders)],
      cmake_args=CMAKE_ARGS,
      classifiers=("Programming Language :: Python :: 3",
                   "Operating System :: OS Independent",
                   "Development Status :: 2 - Pre-Alpha",
                   "Environment :: X11 Applications :: Qt",
                   "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)"),
      install_requires=["scikit-build", "PyOpenGL", "psutil", "qtconsole", "numpy",
                        "matplotlib"],
      entry_points={ "gui_scripts" : "ngsolve = ngsgui.start:main" })

