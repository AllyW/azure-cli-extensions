# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "devcenter dev add-on list",
)
class List(AAZCommand):
    """List addons for this Dev Box.

    :example: List
        az devcenter dev add-on list --project-name "myProject" --user-id "me" --dev-box-name "myDevBox"
    """

    _aaz_info = {
        "version": "2025-04-01-preview",
        "resources": [
            ["data-plane:microsoft.devcenter", "/projects/{}/users/{}/devboxes/{}/addons", "2025-04-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group "Client"

        _args_schema = cls._args_schema
        _args_schema.endpoint = AAZStrArg(
            options=["--endpoint"],
            arg_group="Client",
            help="The API endpoint for the developer resources. Use az configure -d endpoint=<endpoint_uri> to configure a default.",
            required=True,
        )

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.dev_box_name = AAZStrArg(
            options=["--dev-box", "--dev-box-name"],
            help="The name of a Dev Box.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.project_name = AAZStrArg(
            options=["--project", "--project-name"],
            help="The name of the project. Use az configure -d project=<project_name> to configure a default.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.user_id = AAZStrArg(
            options=["--user-id"],
            help="The AAD object id of the user. If value is 'me', the identity is taken from the authentication context.",
            required=True,
            default="me",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9]{8}-([a-zA-Z0-9]{4}-){3}[a-zA-Z0-9]{12}$|^me$",
                max_length=36,
                min_length=2,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DevBoxesListDevBoxAddons(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class DevBoxesListDevBoxAddons(AAZHttpOperation):
        CLIENT_TYPE = "AAZMicrosoftDevcenterDataPlaneClient_devcenter"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/projects/{projectName}/users/{userId}/devboxes/{devBoxName}/addons",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "endpoint", self.ctx.args.endpoint,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "devBoxName", self.ctx.args.dev_box_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "projectName", self.ctx.args.project_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "userId", self.ctx.args.user_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2025-04-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.action_state = AAZStrType(
                serialized_name="actionState",
                flags={"read_only": True},
            )
            _element.error = AAZObjectType(
                flags={"read_only": True},
            )
            _ListHelper._build_schema_azure_core_foundations_error_read(_element.error)
            _element.kind = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            disc_dev_box_tunnel = cls._schema_on_200.value.Element.discriminate_by("kind", "DevBoxTunnel")
            disc_dev_box_tunnel.code_tunnel_name = AAZStrType(
                serialized_name="codeTunnelName",
                flags={"read_only": True},
            )
            disc_dev_box_tunnel.code_tunnel_url = AAZStrType(
                serialized_name="codeTunnelUrl",
                flags={"read_only": True},
            )
            disc_dev_box_tunnel.hosting_resource_name = AAZStrType(
                serialized_name="hostingResourceName",
            )
            disc_dev_box_tunnel.status = AAZStrType(
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_azure_core_foundations_error_read = None

    @classmethod
    def _build_schema_azure_core_foundations_error_read(cls, _schema):
        if cls._schema_azure_core_foundations_error_read is not None:
            _schema.code = cls._schema_azure_core_foundations_error_read.code
            _schema.details = cls._schema_azure_core_foundations_error_read.details
            _schema.innererror = cls._schema_azure_core_foundations_error_read.innererror
            _schema.message = cls._schema_azure_core_foundations_error_read.message
            _schema.target = cls._schema_azure_core_foundations_error_read.target
            return

        cls._schema_azure_core_foundations_error_read = _schema_azure_core_foundations_error_read = AAZObjectType(
            flags={"read_only": True}
        )

        azure_core_foundations_error_read = _schema_azure_core_foundations_error_read
        azure_core_foundations_error_read.code = AAZStrType(
            flags={"required": True},
        )
        azure_core_foundations_error_read.details = AAZListType()
        azure_core_foundations_error_read.innererror = AAZObjectType()
        cls._build_schema_azure_core_foundations_inner_error_read(azure_core_foundations_error_read.innererror)
        azure_core_foundations_error_read.message = AAZStrType(
            flags={"required": True},
        )
        azure_core_foundations_error_read.target = AAZStrType()

        details = _schema_azure_core_foundations_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_azure_core_foundations_error_read(details.Element)

        _schema.code = cls._schema_azure_core_foundations_error_read.code
        _schema.details = cls._schema_azure_core_foundations_error_read.details
        _schema.innererror = cls._schema_azure_core_foundations_error_read.innererror
        _schema.message = cls._schema_azure_core_foundations_error_read.message
        _schema.target = cls._schema_azure_core_foundations_error_read.target

    _schema_azure_core_foundations_inner_error_read = None

    @classmethod
    def _build_schema_azure_core_foundations_inner_error_read(cls, _schema):
        if cls._schema_azure_core_foundations_inner_error_read is not None:
            _schema.code = cls._schema_azure_core_foundations_inner_error_read.code
            _schema.innererror = cls._schema_azure_core_foundations_inner_error_read.innererror
            return

        cls._schema_azure_core_foundations_inner_error_read = _schema_azure_core_foundations_inner_error_read = AAZObjectType()

        azure_core_foundations_inner_error_read = _schema_azure_core_foundations_inner_error_read
        azure_core_foundations_inner_error_read.code = AAZStrType()
        azure_core_foundations_inner_error_read.innererror = AAZObjectType()
        cls._build_schema_azure_core_foundations_inner_error_read(azure_core_foundations_inner_error_read.innererror)

        _schema.code = cls._schema_azure_core_foundations_inner_error_read.code
        _schema.innererror = cls._schema_azure_core_foundations_inner_error_read.innererror


__all__ = ["List"]
