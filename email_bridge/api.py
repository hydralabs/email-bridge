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
Postfix Manager API for Python
"""

from orm import Mailbox
from dovecot import dovecotpw

class MailboxManager():
    """
    Generic API for managing Mailboxes in Postfix
    """
    
    def __init__(self, store):
        self.store = store
    
    def create(self, email, password, name, quota, status):
        
        def gotSuccess(s):
            return "Success"
        
        def gotResult(r):
            return self.store.commit()
        
        def gotError(f):
            self.store.rollback()
            return "Fault"
        
        mb = Mailbox()
        mb.username = unicode(email)
        mb.password = unicode(dovecotpw(password))
        mb.name = unicode(name)
        mb.quota = quota
        mb.status = status
        
        d = self.store.add(mb)
        d.addCallbacks(gotResult, gotError)
        d.addCallbacks(gotSuccess, gotError)
        return d
    
    def update(self, email, password, name, quota, status):
        
        def gotSuccess(s):
            return "Success"
        
        def gotMailbox(mb):
            
            mb.password = unicode(dovecotpw(password))
            mb.name = unicode(name)
            mb.quota = quota
            mb.status = status
            
            return self.store.commit()
        
        def gotError(e):
            self.store.rollback()
            print e
            return "Fault"
        
        d = self.store.get(Mailbox, unicode(email))
        d.addCallbacks(gotMailbox, gotError)
        d.addCallbacks(gotSuccess, gotError)
        return d
        
    
    def delete(self, email):
        q = "DELETE * FROM `%s` WHERE `username` = %s LIMIT 1"
        print q
        
    def disable(self, email):
        
        def gotSuccess(s):
            return "Success"
        
        def gotMailbox(mb):
            
            mb.status = False
            
            return self.store.commit()
        
        def gotError(e):
            self.store.rollback()
            print e
            return "Fault"
        
        d = self.store.get(Mailbox, unicode(email))
        d.addCallbacks(gotMailbox, gotError)
        d.addCallbacks(gotSuccess, gotError)
        return d
        
    def enable(self, email):
        
        def gotSuccess(s):
            return "Success"
        
        def gotMailbox(mb):
            
            mb.status = True
            
            return self.store.commit()
        
        def gotError(e):
            self.store.rollback()
            print e
            return "Fault"
        
        d = self.store.get(Mailbox, unicode(email))
        d.addCallbacks(gotMailbox, gotError)
        d.addCallbacks(gotSuccess, gotError)
        return d