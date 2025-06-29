# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "confluent organization role-binding",
)
class __CMDGroup(AAZCommandGroup):
    """Manage role bindings within a Confluent organization.
    """
    pass


__all__ = ["__CMDGroup"]
