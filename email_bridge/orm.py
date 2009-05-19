# -*- coding: utf-8 -*-
#
# Copyright (C) 2007-2009 Jacob Feisley
# http://feisley.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# $Id$

"""
Objects and Classes to handle operations in the Storm ORM
"""

from storm.locals import *
from storm.twisted.store import *
from storm.twisted.wrapper import *


class Mailbox(Storm):
    __storm_table__ = 'mailbox'
    
    username = Unicode(primary = True)
    password = Unicode()
    name = Unicode()
    quota = Int()
    domain = Unicode()
    created = DateTime()
    modified = DateTime()
    active = Bool()