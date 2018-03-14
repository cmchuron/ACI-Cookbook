__Author__ = "Chip McHuron"
"""Manages login to APICs.

Started life as a simple text builder to generate login URI and body,
but I would like to see it become a full-fledged APIC Login Manager,
so that you could simply call it from all your APIC scripts and it
would use requests to manage future calls to the APIC.

For now, it still just builds text.

"""
import json
import getpass

class RequestBuilder:
    """Creates the URI and body of a JSON request to log in to an APIC.
    
    Args:
        apic (str): The IP or FQDN of the APIC to place the call to.
        user (str): The username to use when connecting.
        pwd (str): The password for the above user.
        
        Note:  If any of these are ommitted, this class will prompt
        the user for input.
        
    To Do:
        Make the Connect() function actually useful.
    """
    
    def __init__(self, apic=None, user=None, pwd=None):
        """
        
        """
        
        self.URI = self.return_login_URI(apic)
        self.body = self.return_login_body(user,pwd)

    def return_login_URI(self, apic=None):
        """Takes a server name, and returns the URI of the API login
        
        Either takes the name of a server as an argument or asks the 
        user to provide one, and returns the URI of the login.

        Args:
            server (str): A DNS resolvable name of the APIC

            Returns:
                A string with the login URI

        """
        
        if apic == None:
            apic = raw_input ('Enter APIC FQDN or IP: ')

        LoginURI = 'https://'+ apic + '/api/aaaLogin.json'
        return str(LoginURI)
        
    def return_login_body(self,user=None, pwd=None):
        """Builds the Body of a login request and returns it.

        Either takes the user's password and login as arguments
        or asks the user for them and returns the body of a login
        request.

        This can be sent to the APIC using POST in order to receive
        a token to be used for future transactions.

        Args:
            user (str): The username to be used for login to the APIC
            pwd (str): The password for the above user (Duh.)

        Returns:
            A string of JSON text that can be used as the login body.

        """
        
        if user == None:
            guess = getpass.getuser()
            user = raw_input ('Username (' + guess +'): ')
            if not user:
                user = guess
                    
        if pwd == None:
            pwd = getpass.getpass()

        #Create the object
        login_body = \
        {'aaaUser': {'attributes': {'name': '', 'pwd': ''}}}

        #Fill in the username and password information
        login_body['aaaUser']['attributes']['name']=user
        login_body['aaaUser']['attributes']['pwd']=pwd

        #Return a string of JSON text
        return json.dumps(login_body)
        
    def Connect(self):
        #Not Built Yet.  For now, just disply output
        print "Connect to : ", self.URI
        print "With the string: ", self.body
