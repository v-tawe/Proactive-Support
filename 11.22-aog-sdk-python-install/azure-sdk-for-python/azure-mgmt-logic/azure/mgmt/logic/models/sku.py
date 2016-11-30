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


class Sku(Model):
    """Sku.

    :param name: The name. Possible values include: 'NotSpecified', 'Free',
     'Shared', 'Basic', 'Standard', 'Premium'
    :type name: str or :class:`SkuName <azure.mgmt.logic.models.SkuName>`
    :param plan: The reference to plan.
    :type plan: :class:`ResourceReference
     <azure.mgmt.logic.models.ResourceReference>`
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'SkuName'},
        'plan': {'key': 'plan', 'type': 'ResourceReference'},
    }

    def __init__(self, name=None, plan=None):
        self.name = name
        self.plan = plan