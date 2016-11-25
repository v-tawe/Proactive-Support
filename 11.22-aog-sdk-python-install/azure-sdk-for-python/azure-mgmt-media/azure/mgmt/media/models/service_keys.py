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


class ServiceKeys(Model):
    """The response body for a ListKeys API.

    :param primary_auth_endpoint: The primary Authorization endpoint.
    :type primary_auth_endpoint: str
    :param secondary_auth_endpoint: The secondary Authorization endpoint.
    :type secondary_auth_endpoint: str
    :param primary_key: The primary resource.
    :type primary_key: str
    :param secondary_key: The secondary resource.
    :type secondary_key: str
    :param scope: The authorization scope.
    :type scope: str
    """ 

    _attribute_map = {
        'primary_auth_endpoint': {'key': 'primaryAuthEndpoint', 'type': 'str'},
        'secondary_auth_endpoint': {'key': 'secondaryAuthEndpoint', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
    }

    def __init__(self, primary_auth_endpoint=None, secondary_auth_endpoint=None, primary_key=None, secondary_key=None, scope=None):
        self.primary_auth_endpoint = primary_auth_endpoint
        self.secondary_auth_endpoint = secondary_auth_endpoint
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.scope = scope
