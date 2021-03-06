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

from .entity_health_state import EntityHealthState


class NodeHealthState(EntityHealthState):
    """Represents the health state of a node, which contains the node identifier
    and its aggregated health state.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or :class:`enum
     <azure.servicefabric.models.enum>`
    :param name:
    :type name: str
    :param id:
    :type id: :class:`NodeId <azure.servicefabric.models.NodeId>`
    """

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'id': {'key': 'Id', 'type': 'NodeId'},
    }

    def __init__(self, aggregated_health_state=None, name=None, id=None):
        super(NodeHealthState, self).__init__(aggregated_health_state=aggregated_health_state)
        self.name = name
        self.id = id
