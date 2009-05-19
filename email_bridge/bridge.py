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

from storm.locals import *
from storm.twisted.store import *

from dovecot import dovecotpw
from api import MailboxManager


class MailboxGateway(xmlrpc.XMLRPC):
    
    manager = None
    
    def xmlrpc_create(self, email, password, name, quota, status):
        return self.manager.create(email, password, name, quota, status)

    def xmlrpc_update(self, email, password, name, quota, status):
        return self.manager.update(email, password, name, quota, status)
    
    def xmlrpc_delete(self, email):
        return 'Not Implemented'
    
    def xmlrpc_disable(self, email):
        return 'Not Implemented'
    
    def xmlrpc_enable(self, email):
        return 'Not Implemented'

database = create_database("mysql://user:pass@host/database")

store = DeferredStore(database)
d = store.start()

def goterr(e):
    print "Db error"
    
def gotstore(s):
    print "got db"
    
d.addCallbacks(gotstore, goterr)

gw = MailboxGateway()
gw.manager = MailboxManager(store)

site = server.Site(gw)