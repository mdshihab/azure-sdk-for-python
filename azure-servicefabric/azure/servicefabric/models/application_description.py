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


class ApplicationDescription(Model):
    """Describes a Service Fabric application.

    :param name:
    :type name: str
    :param type_name:
    :type type_name: str
    :param type_version:
    :type type_version: str
    :param parameter_list:
    :type parameter_list: list of :class:`ApplicationParameter
     <azure.servicefabric.models.ApplicationParameter>`
    :param application_capacity:
    :type application_capacity: :class:`ApplicationCapacityDescription
     <azure.servicefabric.models.ApplicationCapacityDescription>`
    """

    _validation = {
        'name': {'required': True},
        'type_name': {'required': True},
        'type_version': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'type_name': {'key': 'TypeName', 'type': 'str'},
        'type_version': {'key': 'TypeVersion', 'type': 'str'},
        'parameter_list': {'key': 'ParameterList', 'type': '[ApplicationParameter]'},
        'application_capacity': {'key': 'ApplicationCapacity', 'type': 'ApplicationCapacityDescription'},
    }

    def __init__(self, name, type_name, type_version, parameter_list=None, application_capacity=None):
        self.name = name
        self.type_name = type_name
        self.type_version = type_version
        self.parameter_list = parameter_list
        self.application_capacity = application_capacity
