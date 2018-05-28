from simple_salesforce import Salesforce
from simple_salesforce import SFType
import local
import json

__author__ = 'asitm9'

if __name__ == '__main__':
    sf = Salesforce(username=local.username, password=local.password,
                    security_token=local.security_token)
    # print sf.Contact.describe()
    SFType('Account', sf.session_id,
           sf.sf_instance, sf_version=sf.sf_version,
           proxies=sf.proxies, session=sf.session).describe()

