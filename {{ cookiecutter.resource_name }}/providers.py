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


"""Identifier provider."""

from __future__ import absolute_import, print_function

from invenio_pidstore.models import PIDStatus
from invenio_pidstore.providers.base import BaseProvider

from .models import {{ cookiecutter.class_name }}Identifier


class {{ cookiecutter.class_name }}Provider(BaseProvider):
    """{{ cookiecutter.class_name }} identifier provider."""

    pid_type = '{{ cookiecutter.pid_type }}'
    """Type of persistent identifier."""

    pid_identifier = {{ cookiecutter.class_name }}Identifier.__tablename__
    """Identifier for table name"""

    pid_provider = None
    """Provider name.

    The provider name is not recorded in the PID since the provider does not
    provide any additional features besides creation of {{ cookiecutter.class_name }} ids.
    """

    @classmethod
    def create(cls, object_type=None, object_uuid=None, **kwargs):
        """Create a new {{ cookiecutter.class_name }} identifier."""
        assert 'pid_value' not in kwargs
        kwargs['pid_value'] = str({{ cookiecutter.class_name }}Identifier.next())
        kwargs.setdefault('status', cls.default_status)
        if object_type and object_uuid:
            kwargs['status'] = PIDStatus.REGISTERED
        return super({{ cookiecutter.class_name }}Provider, cls).create(
            object_type=object_type, object_uuid=object_uuid, **kwargs)
