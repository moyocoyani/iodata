# -*- coding: utf-8 -*-
# IODATA is an input and output module for quantum chemistry.
#
# Copyright (C) 2011-2019 The IODATA Development Team
#
# This file is part of IODATA.
#
# IODATA is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# IODATA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
# pragma pylint: disable=invalid-name,no-member
"""Test iodata.orca module."""

import numpy as np

from ..iodata import IOData
from ..utils import angstrom
try:
    from importlib_resources import path
except ImportError:
    from importlib.resources import path


def test_load_water_number():
    # test if IOData has atomic numbers
    with path('iodata.test.data', 'water_orca.out') as fn_xyz:
        mol = IOData.from_file(fn_xyz)
    check_water(mol)


def test_load_water_element():
    # test if IOData has atomic symbols
    with path('iodata.test.data', 'water_orca.out') as fn_xyz:
        mol = IOData.from_file(fn_xyz)
    check_water(mol)


def test_load_scf_energy():
    # test if IOData has the correct energy
    with path('iodata.test.data', 'water_orca.out') as fn_xyz:
        mol = IOData.from_file(fn_xyz)
    check_water(mol)


def check_water(mol):
    """Check if atomic numbers and coordinates obtained from orca out file are correct.

    Parameters
    ----------
    mol : IOData
        IOdata dictionary.

    """
    np.testing.assert_equal(mol.numbers, [8, 1, 1])
    # check bond length
    assert abs(np.linalg.norm(mol.coordinates[0] - mol.coordinates[1]) / angstrom - 0.9500) < 1e-5
    assert abs(np.linalg.norm(mol.coordinates[0] - mol.coordinates[2]) / angstrom - 0.9500) < 1e-5
    assert abs(np.linalg.norm(mol.coordinates[1] - mol.coordinates[2]) / angstrom - 1.5513) < 1e-4
    # check scf energy
    assert abs(mol.energy - (-74.959292304818)) < 1e-8


def test_helper_number_atoms():
    # Test if the number of atoms in the ORCA out file is obtained correctly
    with path('iodata.test.data', 'water_orca.out') as fn_xyz:
        mol = IOData.from_file(str(fn_xyz))
    assert mol.natom == 3