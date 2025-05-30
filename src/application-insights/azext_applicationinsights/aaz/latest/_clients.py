# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_client("AAZMicrosoftInsightsDataPlaneClient_application_insights")
class AAZMicrosoftInsightsDataPlaneClient(AAZBaseClient):
    _CLOUD_HOST_TEMPLATES = {
        CloudNameEnum.AzureChinaCloud: "https://api.applicationinsights.azure.cn",
        CloudNameEnum.AzureCloud: "https://api.applicationinsights.io",
        CloudNameEnum.AzureUSGovernment: "https://api.applicationinsights.us",
    }
    _CLOUD_HOST_METADATA_INDEX = "appInsightsResourceId"

    _AAD_CREDENTIAL_SCOPES = [
        "https://api.applicationinsights.io/.default",
    ]

    @classmethod
    def _build_base_url(cls, ctx, **kwargs):
        endpoint = cls.get_cloud_endpoint(ctx, cls._CLOUD_HOST_METADATA_INDEX)
        if not endpoint:
            endpoint = cls._CLOUD_HOST_TEMPLATES.get(ctx.cli_ctx.cloud.name, None)
        return endpoint

    @classmethod
    def _build_configuration(cls, ctx, credential, **kwargs):
        return AAZClientConfiguration(
            credential=credential,
            credential_scopes=cls._AAD_CREDENTIAL_SCOPES,
            **kwargs
        )


class _AAZMicrosoftInsightsDataPlaneClientHelper:
    """Helper class for AAZMicrosoftInsightsDataPlaneClient"""


__all__ = [
    "AAZMicrosoftInsightsDataPlaneClient",
]
