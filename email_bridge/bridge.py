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
Postfix Email XML-RPC api
"""

from twisted.internet import reactor, threads, ssl, defer
from twisted.web import server, resource, static, xmlrpc

from sql import SqlManager
import util

sqldb = SqlManager()

class EmailGateway(xmlrpc.XMLRPC):
    
    def xmlrpc_create(self, email, password, name, quota, status):
        sqldb.create(email, password, name, quota, status)
        return 'Success'

    def xmlrpc_update(self, email, password, name, quota, status):
        #Note: This is not normal as you cannot "change" an email
        
        sqldb.update(email, password, name, quota, status)
        return 'Success'
    
    def xmlrpc_delete(self, email):
        sqldb.delete(email)   
        return 'Success'
    
    def xmlrpc_disable(self, email):
        sqldb.disable(email)
        return 'Success'
    
    def xmlrpc_enable(self, email):
        sqldb.enable(email)
        return 'Success'


site = server.Site(EmailGateway())