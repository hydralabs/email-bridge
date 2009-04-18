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
MySQL mappings for the integration with Postfix
"""

from twisted.enterprise.adbapi import ConnectionPool

class SqlManager():
    
    def __init__(self):
        
        self.table = 'mailbox'
    
        self.db = ConnectionPool(
            "MySQLdb",
            cp_reconnect=True,
            host="server_ip",
            user="username",
            passwd="password",
            db="db_name",
            cp_noisy = True
        )
    
    def create(self, email, password, name, quota, status):
        q = "INSERT OR UPDATE"
    
    def update(self, email, password, name, quota, status):
        q = "UPDATE "
    
    def delete(self, email):
        q = "DELETE * FROM `%s` WHERE `username` = %s LIMIT 1"
        print q
        
    def disable(self, email):
        q = "UPDATE `%s` SET `active` = %s WHERE `username` = '%s' LIMIT 1"
        db.runQuery(q, db_table, 0, email)
        
    def enable(self, email):
        q = "UPDATE `%s` SET `active` = %s WHERE `username` = '%s' LIMIT 1"
        db.runQuery(q, db_table, 1, email)
    