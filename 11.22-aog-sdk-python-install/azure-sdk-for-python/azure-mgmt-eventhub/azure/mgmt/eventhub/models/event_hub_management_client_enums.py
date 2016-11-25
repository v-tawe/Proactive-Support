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

from enum import Enum


class SkuName(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SkuTier(Enum):

    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class NamespaceState(Enum):

    unknown = "Unknown"
    creating = "Creating"
    created = "Created"
    activating = "Activating"
    enabling = "Enabling"
    active = "Active"
    disabling = "Disabling"
    disabled = "Disabled"
    soft_deleting = "SoftDeleting"
    soft_deleted = "SoftDeleted"
    removing = "Removing"
    removed = "Removed"
    failed = "Failed"


class AccessRights(Enum):

    manage = "Manage"
    send = "Send"
    listen = "Listen"


class Policykey(Enum):

    primary_key = "PrimaryKey"
    secondary_key = "SecondaryKey"


class EntityStatus(Enum):

    active = "Active"
    disabled = "Disabled"
    restoring = "Restoring"
    send_disabled = "SendDisabled"
    receive_disabled = "ReceiveDisabled"
    creating = "Creating"
    deleting = "Deleting"
    renaming = "Renaming"
    unknown = "Unknown"
