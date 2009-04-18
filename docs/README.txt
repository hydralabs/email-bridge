==================================
Postfix Email Configuration Bridge
==================================

== Requirements ==

 * Python 2.5
 * Twisted 8.2
 * MySQLdb
 

== Running the Server ==

To run the server use the following command:

  twistd -y bridge.tac
  
By default the server will listen on port 8080, though this can be changed
in bridge.tac
  
You may want to consult the "twistd" documentation for more options such
as logging and dameonizing the application.