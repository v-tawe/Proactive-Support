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


class SharedAccessAuthorizationRuleProperties(Model):
    """SharedAccessAuthorizationRule properties.

    :param rights: The rights associated with the rule.
    :type rights: list of str or :class:`AccessRights
     <azure.mgmt.notificationhubs.models.AccessRights>`
    """ 

    _attribute_map = {
        'rights': {'key': 'rights', 'type': '[AccessRights]'},
    }

    def __init__(self, rights=None):
        self.rights = rights