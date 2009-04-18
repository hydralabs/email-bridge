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
Postfix Email XML-RPC interface
"""

import os
import sys
apppath = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, apppath)

from twisted.web import resource, server
from twisted.application import service, strports

from email_bridge.bridge import site


application = service.Application('Postfix XML-RPC Bridge')
service = strports.service('tcp:8080', site)
service.setServiceParent(application)
