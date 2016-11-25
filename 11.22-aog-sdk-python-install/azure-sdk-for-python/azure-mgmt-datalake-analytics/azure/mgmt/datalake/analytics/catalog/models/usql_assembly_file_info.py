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


class USqlAssemblyFileInfo(Model):
    """A Data Lake Analytics catalog U-SQL assembly file information item.

    :param type: the assembly file type. Possible values include: 'Assembly',
     'Resource'
    :type type: str or :class:`FileType
     <azure.mgmt.datalake.analytics.catalog.models.FileType>`
    :param original_path: the the original path to the assembly file.
    :type original_path: str
    :param content_path: the the content path to the assembly file.
    :type content_path: str
    """ 

    _attribute_map = {
        'type': {'key': 'type', 'type': 'FileType'},
        'original_path': {'key': 'originalPath', 'type': 'str'},
        'content_path': {'key': 'contentPath', 'type': 'str'},
    }

    def __init__(self, type=None, original_path=None, content_path=None):
        self.type = type
        self.original_path = original_path
        self.content_path = content_path
