from simple_salesforce import Salesforce
from simple_salesforce import SFType
import local
import field_mapping as fm
import json

__author__ = 'asitm9'

if __name__ == '__main__':
    sf = Salesforce(username=local.username, password=local.password,
                    security_token=local.security_token)
    # print sf.Contact.describe()
    acoount = SFType('Account', sf.session_id,
           sf.sf_instance, sf_version=sf.sf_version,
           proxies=sf.proxies, session=sf.session).describe()
    ds = sf.describe()
    print sf.__dict__
    f_types = set()
    # for so in ds.get('sobjects'):
    #     if so.get('createable') is True:
    #         # print so.get('name')
    #         so = SFType(so.get('name'),
    #                     sf.session_id,
    #                     sf.sf_instance, sf_version=sf.sf_version,
    #                     proxies=sf.proxies, session=sf.session
    #                     ).describe()
    #         for fld in so.get('fields'):
    #             print '{}\n'.format(fld.get('name'))

    # for fld in acoount.get('fields'):
    #     print 'name -> %s type -> %s' % (fld.get('name'), fld.get('soapType'))
    obj_name = 'Account'
    print 'class {}(models.Model):\n'.format(obj_name)

    for s in acoount.get('fields'):
        print '\t {} = models.{}()\n'.format(s.get('name'), fm.sf2django.get(s.get('soapType')))

