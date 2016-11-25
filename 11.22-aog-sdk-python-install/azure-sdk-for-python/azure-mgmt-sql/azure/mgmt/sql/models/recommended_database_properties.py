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


class RecommendedDatabaseProperties(Model):
    """Represents the properties of a recommended Azure SQL Database being
    upgraded.

    :param name: The name of the Azure SQL Database being upgraded.
    :type name: str
    :param target_edition: The target edition for the Azure SQL Database
     being upgraded. Possible values include: 'Basic', 'Standard', 'Premium',
     'Free', 'Stretch', 'DataWarehouse'
    :type target_edition: str or :class:`TargetDatabaseEditions
     <azure.mgmt.sql.models.TargetDatabaseEditions>`
    :param target_service_level_objective: The target Service Level Objective
     for the Azure SQL Database being upgraded.
    :type target_service_level_objective: str
    """ 

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'target_edition': {'key': 'TargetEdition', 'type': 'str'},
        'target_service_level_objective': {'key': 'TargetServiceLevelObjective', 'type': 'str'},
    }

    def __init__(self, name=None, target_edition=None, target_service_level_objective=None):
        self.name = name
        self.target_edition = target_edition
        self.target_service_level_objective = target_service_level_objective
