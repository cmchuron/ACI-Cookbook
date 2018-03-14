import json
import getpass

class RequestBuilder:
    '''Manages APIC logins
    
    '''

    def return_login_URI(self, apic=None):
        '''Takes a server name, and returns the URI of the API login
        
        Either takes the name of a server as an argument or asks the 
        user to provide one, and returns the URI of the login.

        Args:
            server (str): A DNS resolvable name of the APIC

            Returns:
                A string with the login URI

        '''
        
        if apic == None:
            apic = raw_input ('Enter IP FQDN: ')

        LoginURI = 'https://'+ apic + '/api/aaaLogin.json'
        return str(LoginURI)
        
    def return_login_body(self,user=None, pwd=None):
        '''Builds the Body of a login request and returns it.

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

        '''
        
        if user == None:
            user = raw_input('Enter User: ')
        
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