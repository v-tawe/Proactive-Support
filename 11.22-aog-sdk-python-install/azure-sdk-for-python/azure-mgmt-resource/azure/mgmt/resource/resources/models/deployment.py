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


class Deployment(Model):
    """Deployment operation parameters.

    :param properties: The deployment properties.
    :type properties: :class:`DeploymentProperties
     <azure.mgmt.resource.resources.models.DeploymentProperties>`
    """ 

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'DeploymentProperties'},
    }

    def __init__(self, properties=None):
        self.properties = properties
