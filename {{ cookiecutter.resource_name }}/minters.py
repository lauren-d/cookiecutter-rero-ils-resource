# -*- coding: utf-8 -*-
#
# RERO ILS
# Copyright (C) 2019 RERO
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Identifier minters."""

from __future__ import absolute_import, print_function, unicode_literals

from functools import partial

from .providers import {{ cookiecutter.class_name }}Provider
from ..minters import id_minter

{{ cookiecutter.name }}_id_minter = partial(
    id_minter,
    provider={{ cookiecutter.class_name }}Provider
)
