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
    "connectedmachine run-command create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create a run command.

    :example: Sample command for run-command create
        az connectedmachine run-command create --resource-group myResourceGroup --location "WestUS" --async false --parameters "[{"name":"param1","value":"value1"}]" --password "<runAsPassword>" --user "user1" --script "Write-Host Hello World!" --timeout 3600 --name myRunCommand --machine-name myMachine --subscription mySubscription
        az connectedmachine run-command create --resource-group myResourceGroup --location "WestUS" --script "Write-Host Hello World!" --name myRunCommand --machine-name myMachine --output-uri "outputuri" --subscription mySubscription
    """

    _aaz_info = {
        "version": "2024-11-10-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.hybridcompute/machines/{}/runcommands/{}", "2024-11-10-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.machine_name = AAZStrArg(
            options=["--machine-name"],
            help="The name of the hybrid machine.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="[a-zA-Z0-9-_\.]+",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.run_command_name = AAZStrArg(
            options=["-n", "--name", "--run-command-name"],
            help="The name of the run command.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="[a-zA-Z0-9-_\.]+",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.async_execution = AAZBoolArg(
            options=["--async-execution"],
            arg_group="Properties",
            help="Optional. If set to true, provisioning will complete as soon as script starts and will not wait for script to complete.",
            default=False,
        )
        _args_schema.error_blob_managed_identity = AAZObjectArg(
            options=["--error-blob-id", "--error-blob-managed-identity"],
            arg_group="Properties",
            help="User-assigned managed identity that has access to errorBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer https://aka.ms/ManagedIdentity and https://aka.ms/RunCommandManaged",
        )
        cls._build_args_run_command_managed_identity_create(_args_schema.error_blob_managed_identity)
        _args_schema.error_blob_uri = AAZStrArg(
            options=["--error-blob-uri"],
            arg_group="Properties",
            help="Specifies the Azure storage blob where script error stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer errorBlobManagedIdentity parameter.",
        )
        _args_schema.output_blob_managed_identity = AAZObjectArg(
            options=["--output-blob-id", "--output-blob-managed-identity"],
            arg_group="Properties",
            help="User-assigned managed identity that has access to outputBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer https://aka.ms/ManagedIdentity and https://aka.ms/RunCommandManaged",
        )
        cls._build_args_run_command_managed_identity_create(_args_schema.output_blob_managed_identity)
        _args_schema.output_blob_uri = AAZStrArg(
            options=["--output-blob-uri"],
            arg_group="Properties",
            help="Specifies the Azure storage blob where script output stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer outputBlobManagedIdentity parameter. ",
        )
        _args_schema.parameters = AAZListArg(
            options=["--parameters"],
            arg_group="Properties",
            help="The parameters used by the script.",
        )
        _args_schema.protected_parameters = AAZListArg(
            options=["--protected-parameters"],
            arg_group="Properties",
            help="The parameters used by the script.",
        )
        _args_schema.run_as_password = AAZStrArg(
            options=["--run-as-password"],
            arg_group="Properties",
            help="Specifies the user account password on the machine when executing the run command.",
        )
        _args_schema.run_as_user = AAZStrArg(
            options=["--run-as-user"],
            arg_group="Properties",
            help="Specifies the user account on the machine when executing the run command.",
        )
        _args_schema.timeout_in_seconds = AAZIntArg(
            options=["--timeout-in-seconds"],
            arg_group="Properties",
            help="The timeout in seconds to execute the run command.",
        )

        parameters = cls._args_schema.parameters
        parameters.Element = AAZObjectArg()
        cls._build_args_run_command_input_parameter_create(parameters.Element)

        protected_parameters = cls._args_schema.protected_parameters
        protected_parameters.Element = AAZObjectArg()
        cls._build_args_run_command_input_parameter_create(protected_parameters.Element)

        # define Arg Group "RunCommandProperties"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="RunCommandProperties",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="RunCommandProperties",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Source"

        _args_schema = cls._args_schema
        _args_schema.command_id = AAZStrArg(
            options=["--command-id"],
            arg_group="Source",
            help="Specifies the commandId of predefined built-in script.",
        )
        _args_schema.script = AAZStrArg(
            options=["--script"],
            arg_group="Source",
            help="Specifies the script content to be executed on the machine.",
        )
        _args_schema.script_uri = AAZStrArg(
            options=["--script-uri"],
            arg_group="Source",
            help="Specifies the script download location. It can be either SAS URI of an Azure storage blob with read access or public URI.",
        )
        _args_schema.script_uri_managed_identity = AAZObjectArg(
            options=["--script-uri-id", "--script-uri-managed-identity"],
            arg_group="Source",
            help="User-assigned managed identity that has access to scriptUri in case of Azure storage blob. Use an empty object in case of system-assigned identity. Make sure the Azure storage blob exists, and managed identity has been given access to blob's container with 'Storage Blob Data Reader' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer https://aka.ms/ManagedIdentity and https://aka.ms/RunCommandManaged.",
        )
        cls._build_args_run_command_managed_identity_create(_args_schema.script_uri_managed_identity)
        return cls._args_schema

    _args_run_command_input_parameter_create = None

    @classmethod
    def _build_args_run_command_input_parameter_create(cls, _schema):
        if cls._args_run_command_input_parameter_create is not None:
            _schema.name = cls._args_run_command_input_parameter_create.name
            _schema.value = cls._args_run_command_input_parameter_create.value
            return

        cls._args_run_command_input_parameter_create = AAZObjectArg()

        run_command_input_parameter_create = cls._args_run_command_input_parameter_create
        run_command_input_parameter_create.name = AAZStrArg(
            options=["name"],
            help="The run command parameter name.",
            required=True,
        )
        run_command_input_parameter_create.value = AAZStrArg(
            options=["value"],
            help="The run command parameter value.",
            required=True,
        )

        _schema.name = cls._args_run_command_input_parameter_create.name
        _schema.value = cls._args_run_command_input_parameter_create.value

    _args_run_command_managed_identity_create = None

    @classmethod
    def _build_args_run_command_managed_identity_create(cls, _schema):
        if cls._args_run_command_managed_identity_create is not None:
            _schema.client_id = cls._args_run_command_managed_identity_create.client_id
            _schema.object_id = cls._args_run_command_managed_identity_create.object_id
            return

        cls._args_run_command_managed_identity_create = AAZObjectArg()

        run_command_managed_identity_create = cls._args_run_command_managed_identity_create
        run_command_managed_identity_create.client_id = AAZStrArg(
            options=["client-id"],
            help="Client Id (GUID value) of the user-assigned managed identity. ObjectId should not be used if this is provided.",
        )
        run_command_managed_identity_create.object_id = AAZStrArg(
            options=["object-id"],
            help="Object Id (GUID value) of the user-assigned managed identity. ClientId should not be used if this is provided.",
        )

        _schema.client_id = cls._args_run_command_managed_identity_create.client_id
        _schema.object_id = cls._args_run_command_managed_identity_create.object_id

    def _execute_operations(self):
        self.pre_operations()
        yield self.MachineRunCommandsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class MachineRunCommandsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridCompute/machines/{machineName}/runCommands/{runCommandName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "machineName", self.ctx.args.machine_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "runCommandName", self.ctx.args.run_command_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-11-10-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("asyncExecution", AAZBoolType, ".async_execution")
                _CreateHelper._build_schema_run_command_managed_identity_create(properties.set_prop("errorBlobManagedIdentity", AAZObjectType, ".error_blob_managed_identity"))
                properties.set_prop("errorBlobUri", AAZStrType, ".error_blob_uri")
                _CreateHelper._build_schema_run_command_managed_identity_create(properties.set_prop("outputBlobManagedIdentity", AAZObjectType, ".output_blob_managed_identity"))
                properties.set_prop("outputBlobUri", AAZStrType, ".output_blob_uri")
                properties.set_prop("parameters", AAZListType, ".parameters")
                properties.set_prop("protectedParameters", AAZListType, ".protected_parameters")
                properties.set_prop("runAsPassword", AAZStrType, ".run_as_password", typ_kwargs={"flags": {"secret": True}})
                properties.set_prop("runAsUser", AAZStrType, ".run_as_user")
                properties.set_prop("source", AAZObjectType)
                properties.set_prop("timeoutInSeconds", AAZIntType, ".timeout_in_seconds")

            parameters = _builder.get(".properties.parameters")
            if parameters is not None:
                _CreateHelper._build_schema_run_command_input_parameter_create(parameters.set_elements(AAZObjectType, "."))

            protected_parameters = _builder.get(".properties.protectedParameters")
            if protected_parameters is not None:
                _CreateHelper._build_schema_run_command_input_parameter_create(protected_parameters.set_elements(AAZObjectType, "."))

            source = _builder.get(".properties.source")
            if source is not None:
                source.set_prop("commandId", AAZStrType, ".command_id")
                source.set_prop("script", AAZStrType, ".script")
                source.set_prop("scriptUri", AAZStrType, ".script_uri")
                _CreateHelper._build_schema_run_command_managed_identity_create(source.set_prop("scriptUriManagedIdentity", AAZObjectType, ".script_uri_managed_identity"))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.async_execution = AAZBoolType(
                serialized_name="asyncExecution",
            )
            properties.error_blob_managed_identity = AAZObjectType(
                serialized_name="errorBlobManagedIdentity",
            )
            _CreateHelper._build_schema_run_command_managed_identity_read(properties.error_blob_managed_identity)
            properties.error_blob_uri = AAZStrType(
                serialized_name="errorBlobUri",
            )
            properties.instance_view = AAZObjectType(
                serialized_name="instanceView",
                flags={"read_only": True},
            )
            properties.output_blob_managed_identity = AAZObjectType(
                serialized_name="outputBlobManagedIdentity",
            )
            _CreateHelper._build_schema_run_command_managed_identity_read(properties.output_blob_managed_identity)
            properties.output_blob_uri = AAZStrType(
                serialized_name="outputBlobUri",
            )
            properties.parameters = AAZListType()
            properties.protected_parameters = AAZListType(
                serialized_name="protectedParameters",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.run_as_password = AAZStrType(
                serialized_name="runAsPassword",
                flags={"secret": True},
            )
            properties.run_as_user = AAZStrType(
                serialized_name="runAsUser",
            )
            properties.source = AAZObjectType()
            properties.timeout_in_seconds = AAZIntType(
                serialized_name="timeoutInSeconds",
            )

            instance_view = cls._schema_on_200_201.properties.instance_view
            instance_view.end_time = AAZStrType(
                serialized_name="endTime",
            )
            instance_view.error = AAZStrType()
            instance_view.execution_message = AAZStrType(
                serialized_name="executionMessage",
            )
            instance_view.execution_state = AAZStrType(
                serialized_name="executionState",
            )
            instance_view.exit_code = AAZIntType(
                serialized_name="exitCode",
            )
            instance_view.output = AAZStrType()
            instance_view.start_time = AAZStrType(
                serialized_name="startTime",
            )
            instance_view.statuses = AAZListType()

            statuses = cls._schema_on_200_201.properties.instance_view.statuses
            statuses.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.instance_view.statuses.Element
            _element.code = AAZStrType()
            _element.display_status = AAZStrType(
                serialized_name="displayStatus",
            )
            _element.level = AAZStrType()
            _element.message = AAZStrType()
            _element.time = AAZStrType()

            parameters = cls._schema_on_200_201.properties.parameters
            parameters.Element = AAZObjectType()
            _CreateHelper._build_schema_run_command_input_parameter_read(parameters.Element)

            protected_parameters = cls._schema_on_200_201.properties.protected_parameters
            protected_parameters.Element = AAZObjectType()
            _CreateHelper._build_schema_run_command_input_parameter_read(protected_parameters.Element)

            source = cls._schema_on_200_201.properties.source
            source.command_id = AAZStrType(
                serialized_name="commandId",
            )
            source.script = AAZStrType()
            source.script_uri = AAZStrType(
                serialized_name="scriptUri",
            )
            source.script_uri_managed_identity = AAZObjectType(
                serialized_name="scriptUriManagedIdentity",
            )
            _CreateHelper._build_schema_run_command_managed_identity_read(source.script_uri_managed_identity)

            system_data = cls._schema_on_200_201.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_run_command_input_parameter_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

    @classmethod
    def _build_schema_run_command_managed_identity_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("clientId", AAZStrType, ".client_id")
        _builder.set_prop("objectId", AAZStrType, ".object_id")

    _schema_run_command_input_parameter_read = None

    @classmethod
    def _build_schema_run_command_input_parameter_read(cls, _schema):
        if cls._schema_run_command_input_parameter_read is not None:
            _schema.name = cls._schema_run_command_input_parameter_read.name
            _schema.value = cls._schema_run_command_input_parameter_read.value
            return

        cls._schema_run_command_input_parameter_read = _schema_run_command_input_parameter_read = AAZObjectType()

        run_command_input_parameter_read = _schema_run_command_input_parameter_read
        run_command_input_parameter_read.name = AAZStrType(
            flags={"required": True},
        )
        run_command_input_parameter_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.name = cls._schema_run_command_input_parameter_read.name
        _schema.value = cls._schema_run_command_input_parameter_read.value

    _schema_run_command_managed_identity_read = None

    @classmethod
    def _build_schema_run_command_managed_identity_read(cls, _schema):
        if cls._schema_run_command_managed_identity_read is not None:
            _schema.client_id = cls._schema_run_command_managed_identity_read.client_id
            _schema.object_id = cls._schema_run_command_managed_identity_read.object_id
            return

        cls._schema_run_command_managed_identity_read = _schema_run_command_managed_identity_read = AAZObjectType()

        run_command_managed_identity_read = _schema_run_command_managed_identity_read
        run_command_managed_identity_read.client_id = AAZStrType(
            serialized_name="clientId",
        )
        run_command_managed_identity_read.object_id = AAZStrType(
            serialized_name="objectId",
        )

        _schema.client_id = cls._schema_run_command_managed_identity_read.client_id
        _schema.object_id = cls._schema_run_command_managed_identity_read.object_id


__all__ = ["Create"]
