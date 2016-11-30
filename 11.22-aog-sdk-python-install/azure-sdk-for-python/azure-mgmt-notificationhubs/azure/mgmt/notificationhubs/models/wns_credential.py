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


class WnsCredential(Model):
    """Description of a NotificationHub WnsCredential.

    :param package_sid: The package ID for this credential.
    :type package_sid: str
    :param secret_key: The secret key.
    :type secret_key: str
    :param windows_live_endpoint: The Windows Live endpoint.
    :type windows_live_endpoint: str
    """ 

    _attribute_map = {
        'package_sid': {'key': 'properties.packageSid', 'type': 'str'},
        'secret_key': {'key': 'properties.secretKey', 'type': 'str'},
        'windows_live_endpoint': {'key': 'properties.windowsLiveEndpoint', 'type': 'str'},
    }

    def __init__(self, package_sid=None, secret_key=None, windows_live_endpoint=None):
        self.package_sid = package_sid
        self.secret_key = secret_key
        self.windows_live_endpoint = windows_live_endpoint