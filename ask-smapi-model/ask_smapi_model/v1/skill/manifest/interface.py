# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum
from abc import ABCMeta, abstractmethod


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime


class Interface(object):
    """

    :param object_type: 
    :type object_type: (optional) str

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``type`` variable.

        | ALEXA_PRESENTATION_APL: :py:class:`ask_smapi_model.v1.skill.manifest.alexa_presentation_apl_interface.AlexaPresentationAplInterface`,
        |
        | APP_LINKS: :py:class:`ask_smapi_model.v1.skill.manifest.app_link_interface.AppLinkInterface`,
        |
        | ALEXA_PRESENTATION_HTML: :py:class:`ask_smapi_model.v1.skill.manifest.alexa_presentation_html_interface.AlexaPresentationHtmlInterface`,
        |
        | AUDIO_PLAYER: :py:class:`ask_smapi_model.v1.skill.manifest.audio_interface.AudioInterface`,
        |
        | GAME_ENGINE: :py:class:`ask_smapi_model.v1.skill.manifest.game_engine_interface.GameEngineInterface`,
        |
        | APP_LINKS_V2: :py:class:`ask_smapi_model.v1.skill.manifest.app_link_v2_interface.AppLinkV2Interface`,
        |
        | RENDER_TEMPLATE: :py:class:`ask_smapi_model.v1.skill.manifest.display_interface.DisplayInterface`,
        |
        | GADGET_CONTROLLER: :py:class:`ask_smapi_model.v1.skill.manifest.gadget_controller_interface.GadgetControllerInterface`,
        |
        | VIDEO_APP: :py:class:`ask_smapi_model.v1.skill.manifest.video_app_interface.VideoAppInterface`

    """
    deserialized_types = {
        'object_type': 'str'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type'
    }  # type: Dict
    supports_multiple_types = False

    discriminator_value_class_map = {
        'ALEXA_PRESENTATION_APL': 'ask_smapi_model.v1.skill.manifest.alexa_presentation_apl_interface.AlexaPresentationAplInterface',
        'APP_LINKS': 'ask_smapi_model.v1.skill.manifest.app_link_interface.AppLinkInterface',
        'ALEXA_PRESENTATION_HTML': 'ask_smapi_model.v1.skill.manifest.alexa_presentation_html_interface.AlexaPresentationHtmlInterface',
        'AUDIO_PLAYER': 'ask_smapi_model.v1.skill.manifest.audio_interface.AudioInterface',
        'GAME_ENGINE': 'ask_smapi_model.v1.skill.manifest.game_engine_interface.GameEngineInterface',
        'APP_LINKS_V2': 'ask_smapi_model.v1.skill.manifest.app_link_v2_interface.AppLinkV2Interface',
        'RENDER_TEMPLATE': 'ask_smapi_model.v1.skill.manifest.display_interface.DisplayInterface',
        'GADGET_CONTROLLER': 'ask_smapi_model.v1.skill.manifest.gadget_controller_interface.GadgetControllerInterface',
        'VIDEO_APP': 'ask_smapi_model.v1.skill.manifest.video_app_interface.VideoAppInterface'
    }

    json_discriminator_key = "type"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, object_type=None):
        # type: (Optional[str]) -> None
        """

        :param object_type: 
        :type object_type: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.object_type = object_type

    @classmethod
    def get_real_child_model(cls, data):
        # type: (Dict[str, str]) -> Optional[str]
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[cls.json_discriminator_key]
        return cls.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
