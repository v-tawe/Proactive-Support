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


class SkuInfo(Model):
    """Sku discovery information.

    :param resource_type: Resource type that this sku applies to
    :type resource_type: str
    :param sku: Name and tier of the sku
    :type sku: :class:`SkuDescription <azure.mgmt.web.models.SkuDescription>`
    :param capacity: Min, max, and default scale values of the sku
    :type capacity: :class:`SkuCapacity <azure.mgmt.web.models.SkuCapacity>`
    """ 

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'SkuDescription'},
        'capacity': {'key': 'capacity', 'type': 'SkuCapacity'},
    }

    def __init__(self, resource_type=None, sku=None, capacity=None):
        self.resource_type = resource_type
        self.sku = sku
        self.capacity = capacity
