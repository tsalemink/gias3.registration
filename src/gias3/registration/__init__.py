"""
GIAS, a library for Geometry, Image Analysis, and Statistics.
Copyright (C) 2014 Ju Zhang
    
This file is part of GIAS. (https://bitbucket.org/jangle/gias)

    GIAS is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    GIAS is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with GIAS.  If not, see <http://www.gnu.org/licenses/>..
"""
from gias3.registration.version import __version__
from gias3.registration.RBF import rbfRegNPass
from gias3.registration.alignment_fitting import *
from gias3.registration.shapemodel import fitSSMTo3DPoints
