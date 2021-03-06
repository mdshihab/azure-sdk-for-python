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


class Trigger(Model):
    """Azure data factory nested object which contains information about creating
    pipeline run.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: BlobTrigger, ScheduleTrigger

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param description: Trigger description.
    :type description: str
    :param pipelines: Pipelines that need to be started.
    :type pipelines:
     list[~azure.mgmt.datafactory.models.TriggerPipelineReference]
    :ivar runtime_state: Indicates if trigger is running or not. Updated when
     Start/Stop APIs are called on the Trigger. Possible values include:
     'Started', 'Stopped', 'Disabled'
    :vartype runtime_state: str or
     ~azure.mgmt.datafactory.models.TriggerRuntimeState
    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'runtime_state': {'readonly': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'pipelines': {'key': 'pipelines', 'type': '[TriggerPipelineReference]'},
        'runtime_state': {'key': 'runtimeState', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'BlobTrigger': 'BlobTrigger', 'ScheduleTrigger': 'ScheduleTrigger'}
    }

    def __init__(self, description=None, pipelines=None):
        self.description = description
        self.pipelines = pipelines
        self.runtime_state = None
        self.type = None
