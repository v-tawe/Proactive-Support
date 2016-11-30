# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AADObject(Model):
    """The properties of an Active Directory object.

    :param object_id: The ID of the object.
    :type object_id: str
    :param object_type: The type of AAD object.
    :type object_type: str
    :param display_name: The display name of the object.
    :type display_name: str
    :param user_principal_name: The principal name of the object.
    :type user_principal_name: str
    :param mail: The primary email address of the object.
    :type mail: str
    :param mail_enabled: Whether the AAD object is mail-enabled.
    :type mail_enabled: bool
    :param security_enabled: Whether the AAD object is security-enabled.
    :type security_enabled: bool
    :param sign_in_name: The sign-in name of the object.
    :type sign_in_name: str
    :param service_principal_names: A collection of service principal names
     associated with the object.
    :type service_principal_names: list of str
    :param user_type: The user type of the object.
    :type user_type: str
    """ 

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'mail_enabled': {'key': 'mailEnabled', 'type': 'bool'},
        'security_enabled': {'key': 'securityEnabled', 'type': 'bool'},
        'sign_in_name': {'key': 'signInName', 'type': 'str'},
        'service_principal_names': {'key': 'servicePrincipalNames', 'type': '[str]'},
        'user_type': {'key': 'userType', 'type': 'str'},
    }

    def __init__(self, object_id=None, object_type=None, display_name=None, user_principal_name=None, mail=None, mail_enabled=None, security_enabled=None, sign_in_name=None, service_principal_names=None, user_type=None):
        self.object_id = object_id
        self.object_type = object_type
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.mail = mail
        self.mail_enabled = mail_enabled
        self.security_enabled = security_enabled
        self.sign_in_name = sign_in_name
        self.service_principal_names = service_principal_names
        self.user_type = user_type