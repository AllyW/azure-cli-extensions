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
    "networkfabric nni update",
)
class Update(AAZCommand):
    """Update the Network to Network interconnect resource

    :example: Update the Network To Network Interconnect
        az networkfabric nni update --resource-group "example-rg" --fabric "example-fabric" --resource-name "example-nni" --import-route-policy "{importIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',importIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}" --export-route-policy "{exportIpv4RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy',exportIpv6RoutePolicyId:'/subscriptions/xxxxx-xxxx-xxxx-xxxx-xxxxx/resourceGroups/example-rg/providers/microsoft.managednetworkfabric/routePolicies/example-routepolicy'}" --layer2-configuration "{interfaces:['resourceId'],mtu:1500}" --option-b-layer3-configuration "{peerASN:28,vlanId:501,primaryIpv4Prefix:'172.31.0.0/31',secondaryIpv4Prefix:'172.31.0.20/31'}"

    :example: Help text for sub parameters under the specific parent can be viewed by using the shorthand syntax '??'. See https://github.com/Azure/azure-cli/tree/dev/doc/shorthand_syntax.md for more about shorthand syntax.
        az networkfabric nni update --layer2-configuration "??"
    """

    _aaz_info = {
        "version": "2024-02-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkfabrics/{}/networktonetworkinterconnects/{}", "2024-02-15-preview"],
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
        _args_schema.fabric_name = AAZStrArg(
            options=["--fabric", "--fabric-name"],
            help="Name of the Network Fabric.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the Network to Network Interconnect.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.egress_acl_id = AAZResourceIdArg(
            options=["--egress-acl-id"],
            arg_group="Properties",
            help="Egress Acl ARM resource ID.",
            nullable=True,
        )
        _args_schema.export_route_policy = AAZObjectArg(
            options=["--export-route-policy"],
            arg_group="Properties",
            help="Export Route Policy information",
        )
        _args_schema.import_route_policy = AAZObjectArg(
            options=["--import-route-policy"],
            arg_group="Properties",
            help="Import Route Policy information.",
        )
        _args_schema.ingress_acl_id = AAZResourceIdArg(
            options=["--ingress-acl-id"],
            arg_group="Properties",
            help="Ingress Acl ARM resource ID.",
            nullable=True,
        )
        _args_schema.layer2_configuration = AAZObjectArg(
            options=["--layer2-configuration"],
            arg_group="Properties",
            help="Common properties for Layer2Configuration.",
        )
        _args_schema.npb_static_route_configuration = AAZObjectArg(
            options=["--npb-static-route-configuration"],
            arg_group="Properties",
            help="NPB Static Route Configuration properties.",
        )
        _args_schema.option_b_layer3_configuration = AAZObjectArg(
            options=["--option-b-layer3-configuration"],
            arg_group="Properties",
            help="Common properties for Layer3Configuration.",
        )

        export_route_policy = cls._args_schema.export_route_policy
        export_route_policy.export_ipv4_route_policy_id = AAZResourceIdArg(
            options=["export-ipv4-route-policy-id"],
            help="Export IPv4 Route Policy Id.",
            nullable=True,
        )
        export_route_policy.export_ipv6_route_policy_id = AAZResourceIdArg(
            options=["export-ipv6-route-policy-id"],
            help="Export IPv6 Route Policy Id.",
            nullable=True,
        )

        import_route_policy = cls._args_schema.import_route_policy
        import_route_policy.import_ipv4_route_policy_id = AAZResourceIdArg(
            options=["import-ipv4-route-policy-id"],
            help="Import IPv4 Route Policy Id.",
            nullable=True,
        )
        import_route_policy.import_ipv6_route_policy_id = AAZResourceIdArg(
            options=["import-ipv6-route-policy-id"],
            help="Import IPv6 Route Policy Id.",
            nullable=True,
        )

        layer2_configuration = cls._args_schema.layer2_configuration
        layer2_configuration.interfaces = AAZListArg(
            options=["interfaces"],
            help="List of network device interfaces resource IDs.",
            fmt=AAZListArgFormat(
                min_length=1,
            ),
        )
        layer2_configuration.mtu = AAZIntArg(
            options=["mtu"],
            help="MTU of the packets between PE & CE. The value should be between 64 and 9200.",
            fmt=AAZIntArgFormat(
                maximum=9200,
                minimum=64,
            ),
        )

        interfaces = cls._args_schema.layer2_configuration.interfaces
        interfaces.Element = AAZResourceIdArg()

        npb_static_route_configuration = cls._args_schema.npb_static_route_configuration
        npb_static_route_configuration.bfd_configuration = AAZObjectArg(
            options=["bfd-configuration"],
            help="BFD Configuration properties.",
        )
        npb_static_route_configuration.ipv4_routes = AAZListArg(
            options=["ipv4-routes"],
            help="List of IPv4 Routes.",
            fmt=AAZListArgFormat(
                min_length=1,
            ),
        )
        npb_static_route_configuration.ipv6_routes = AAZListArg(
            options=["ipv6-routes"],
            help="List of IPv6 Routes.",
            fmt=AAZListArgFormat(
                min_length=1,
            ),
        )

        bfd_configuration = cls._args_schema.npb_static_route_configuration.bfd_configuration
        bfd_configuration.interval_in_milli_seconds = AAZIntArg(
            options=["interval-in-milli-seconds"],
            help="Interval in milliseconds. Default value is 300. Example: 300.",
        )
        bfd_configuration.multiplier = AAZIntArg(
            options=["multiplier"],
            help="Multiplier for the Bfd Configuration. Default value is 5. Example: 5.",
        )

        ipv4_routes = cls._args_schema.npb_static_route_configuration.ipv4_routes
        ipv4_routes.Element = AAZObjectArg()
        cls._build_args_static_route_properties_update(ipv4_routes.Element)

        ipv6_routes = cls._args_schema.npb_static_route_configuration.ipv6_routes
        ipv6_routes.Element = AAZObjectArg()
        cls._build_args_static_route_properties_update(ipv6_routes.Element)

        option_b_layer3_configuration = cls._args_schema.option_b_layer3_configuration
        option_b_layer3_configuration.peer_asn = AAZIntArg(
            options=["peer-asn"],
            help="ASN of PE devices for CE/PE connectivity. The value should be between 1 to 4294967295. Example: 28.",
            fmt=AAZIntArgFormat(
                maximum=4294967295,
                minimum=1,
            ),
        )
        option_b_layer3_configuration.primary_ipv4_prefix = AAZStrArg(
            options=["primary-ipv4-prefix"],
            help="IPv4 Address Prefix. Example: 172.31.0.0/31.",
        )
        option_b_layer3_configuration.primary_ipv6_prefix = AAZStrArg(
            options=["primary-ipv6-prefix"],
            help="IPv6 Address Prefix. Example: 3FFE:FFFF:0:CD30::a0/127.",
            nullable=True,
        )
        option_b_layer3_configuration.secondary_ipv4_prefix = AAZStrArg(
            options=["secondary-ipv4-prefix"],
            help="Secondary IPv4 Address Prefix. Example: 172.31.0.20/31.",
        )
        option_b_layer3_configuration.secondary_ipv6_prefix = AAZStrArg(
            options=["secondary-ipv6-prefix"],
            help="Secondary IPv6 Address Prefix. Example: 3FFE:FFFF:0:CD30::a4/127.",
            nullable=True,
        )
        option_b_layer3_configuration.vlan_id = AAZIntArg(
            options=["vlan-id"],
            help="VLAN for CE/PE Layer 3 connectivity. The value should be between 100 to 4094. Example: 501.",
            fmt=AAZIntArgFormat(
                maximum=4094,
                minimum=100,
            ),
        )
        return cls._args_schema

    _args_static_route_properties_update = None

    @classmethod
    def _build_args_static_route_properties_update(cls, _schema):
        if cls._args_static_route_properties_update is not None:
            _schema.next_hop = cls._args_static_route_properties_update.next_hop
            _schema.prefix = cls._args_static_route_properties_update.prefix
            return

        cls._args_static_route_properties_update = AAZObjectArg()

        static_route_properties_update = cls._args_static_route_properties_update
        static_route_properties_update.next_hop = AAZListArg(
            options=["next-hop"],
            help="List of next hop addresses.",
            required=True,
            fmt=AAZListArgFormat(
                min_length=1,
            ),
        )
        static_route_properties_update.prefix = AAZStrArg(
            options=["prefix"],
            help="Prefix of the route.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        next_hop = cls._args_static_route_properties_update.next_hop
        next_hop.Element = AAZStrArg(
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        _schema.next_hop = cls._args_static_route_properties_update.next_hop
        _schema.prefix = cls._args_static_route_properties_update.prefix

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetworkToNetworkInterconnectsUpdate(ctx=self.ctx)()
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

    class NetworkToNetworkInterconnectsUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects/{networkToNetworkInterconnectName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkFabricName", self.ctx.args.fabric_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkToNetworkInterconnectName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
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
                    "api-version", "2024-02-15-preview",
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
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("egressAclId", AAZStrType, ".egress_acl_id", typ_kwargs={"nullable": True})
                properties.set_prop("exportRoutePolicy", AAZObjectType, ".export_route_policy")
                properties.set_prop("importRoutePolicy", AAZObjectType, ".import_route_policy")
                properties.set_prop("ingressAclId", AAZStrType, ".ingress_acl_id", typ_kwargs={"nullable": True})
                properties.set_prop("layer2Configuration", AAZObjectType, ".layer2_configuration")
                properties.set_prop("npbStaticRouteConfiguration", AAZObjectType, ".npb_static_route_configuration")
                properties.set_prop("optionBLayer3Configuration", AAZObjectType, ".option_b_layer3_configuration")

            export_route_policy = _builder.get(".properties.exportRoutePolicy")
            if export_route_policy is not None:
                export_route_policy.set_prop("exportIpv4RoutePolicyId", AAZStrType, ".export_ipv4_route_policy_id", typ_kwargs={"nullable": True})
                export_route_policy.set_prop("exportIpv6RoutePolicyId", AAZStrType, ".export_ipv6_route_policy_id", typ_kwargs={"nullable": True})

            import_route_policy = _builder.get(".properties.importRoutePolicy")
            if import_route_policy is not None:
                import_route_policy.set_prop("importIpv4RoutePolicyId", AAZStrType, ".import_ipv4_route_policy_id", typ_kwargs={"nullable": True})
                import_route_policy.set_prop("importIpv6RoutePolicyId", AAZStrType, ".import_ipv6_route_policy_id", typ_kwargs={"nullable": True})

            layer2_configuration = _builder.get(".properties.layer2Configuration")
            if layer2_configuration is not None:
                layer2_configuration.set_prop("interfaces", AAZListType, ".interfaces")
                layer2_configuration.set_prop("mtu", AAZIntType, ".mtu")

            interfaces = _builder.get(".properties.layer2Configuration.interfaces")
            if interfaces is not None:
                interfaces.set_elements(AAZStrType, ".")

            npb_static_route_configuration = _builder.get(".properties.npbStaticRouteConfiguration")
            if npb_static_route_configuration is not None:
                npb_static_route_configuration.set_prop("bfdConfiguration", AAZObjectType, ".bfd_configuration")
                npb_static_route_configuration.set_prop("ipv4Routes", AAZListType, ".ipv4_routes")
                npb_static_route_configuration.set_prop("ipv6Routes", AAZListType, ".ipv6_routes")

            bfd_configuration = _builder.get(".properties.npbStaticRouteConfiguration.bfdConfiguration")
            if bfd_configuration is not None:
                bfd_configuration.set_prop("intervalInMilliSeconds", AAZIntType, ".interval_in_milli_seconds")
                bfd_configuration.set_prop("multiplier", AAZIntType, ".multiplier")

            ipv4_routes = _builder.get(".properties.npbStaticRouteConfiguration.ipv4Routes")
            if ipv4_routes is not None:
                _UpdateHelper._build_schema_static_route_properties_update(ipv4_routes.set_elements(AAZObjectType, "."))

            ipv6_routes = _builder.get(".properties.npbStaticRouteConfiguration.ipv6Routes")
            if ipv6_routes is not None:
                _UpdateHelper._build_schema_static_route_properties_update(ipv6_routes.set_elements(AAZObjectType, "."))

            option_b_layer3_configuration = _builder.get(".properties.optionBLayer3Configuration")
            if option_b_layer3_configuration is not None:
                option_b_layer3_configuration.set_prop("peerASN", AAZIntType, ".peer_asn")
                option_b_layer3_configuration.set_prop("primaryIpv4Prefix", AAZStrType, ".primary_ipv4_prefix")
                option_b_layer3_configuration.set_prop("primaryIpv6Prefix", AAZStrType, ".primary_ipv6_prefix", typ_kwargs={"nullable": True})
                option_b_layer3_configuration.set_prop("secondaryIpv4Prefix", AAZStrType, ".secondary_ipv4_prefix")
                option_b_layer3_configuration.set_prop("secondaryIpv6Prefix", AAZStrType, ".secondary_ipv6_prefix", typ_kwargs={"nullable": True})
                option_b_layer3_configuration.set_prop("vlanId", AAZIntType, ".vlan_id")

            return self.serialize_content(_content_value)

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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.egress_acl_id = AAZStrType(
                serialized_name="egressAclId",
                nullable=True,
            )
            properties.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            properties.import_route_policy = AAZObjectType(
                serialized_name="importRoutePolicy",
            )
            properties.ingress_acl_id = AAZStrType(
                serialized_name="ingressAclId",
                nullable=True,
            )
            properties.is_management_type = AAZStrType(
                serialized_name="isManagementType",
            )
            properties.layer2_configuration = AAZObjectType(
                serialized_name="layer2Configuration",
            )
            properties.nni_type = AAZStrType(
                serialized_name="nniType",
            )
            properties.npb_static_route_configuration = AAZObjectType(
                serialized_name="npbStaticRouteConfiguration",
            )
            properties.option_b_layer3_configuration = AAZObjectType(
                serialized_name="optionBLayer3Configuration",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.use_option_b = AAZStrType(
                serialized_name="useOptionB",
                flags={"required": True},
            )

            export_route_policy = cls._schema_on_200.properties.export_route_policy
            export_route_policy.export_ipv4_route_policy_id = AAZStrType(
                serialized_name="exportIpv4RoutePolicyId",
                nullable=True,
            )
            export_route_policy.export_ipv6_route_policy_id = AAZStrType(
                serialized_name="exportIpv6RoutePolicyId",
                nullable=True,
            )

            import_route_policy = cls._schema_on_200.properties.import_route_policy
            import_route_policy.import_ipv4_route_policy_id = AAZStrType(
                serialized_name="importIpv4RoutePolicyId",
                nullable=True,
            )
            import_route_policy.import_ipv6_route_policy_id = AAZStrType(
                serialized_name="importIpv6RoutePolicyId",
                nullable=True,
            )

            layer2_configuration = cls._schema_on_200.properties.layer2_configuration
            layer2_configuration.interfaces = AAZListType()
            layer2_configuration.mtu = AAZIntType()

            interfaces = cls._schema_on_200.properties.layer2_configuration.interfaces
            interfaces.Element = AAZStrType()

            npb_static_route_configuration = cls._schema_on_200.properties.npb_static_route_configuration
            npb_static_route_configuration.bfd_configuration = AAZObjectType(
                serialized_name="bfdConfiguration",
            )
            npb_static_route_configuration.ipv4_routes = AAZListType(
                serialized_name="ipv4Routes",
            )
            npb_static_route_configuration.ipv6_routes = AAZListType(
                serialized_name="ipv6Routes",
            )

            bfd_configuration = cls._schema_on_200.properties.npb_static_route_configuration.bfd_configuration
            bfd_configuration.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            bfd_configuration.interval_in_milli_seconds = AAZIntType(
                serialized_name="intervalInMilliSeconds",
            )
            bfd_configuration.multiplier = AAZIntType()

            ipv4_routes = cls._schema_on_200.properties.npb_static_route_configuration.ipv4_routes
            ipv4_routes.Element = AAZObjectType()
            _UpdateHelper._build_schema_static_route_properties_read(ipv4_routes.Element)

            ipv6_routes = cls._schema_on_200.properties.npb_static_route_configuration.ipv6_routes
            ipv6_routes.Element = AAZObjectType()
            _UpdateHelper._build_schema_static_route_properties_read(ipv6_routes.Element)

            option_b_layer3_configuration = cls._schema_on_200.properties.option_b_layer3_configuration
            option_b_layer3_configuration.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"read_only": True},
            )
            option_b_layer3_configuration.peer_asn = AAZIntType(
                serialized_name="peerASN",
                flags={"required": True},
            )
            option_b_layer3_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
            )
            option_b_layer3_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
                nullable=True,
            )
            option_b_layer3_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
            )
            option_b_layer3_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
                nullable=True,
            )
            option_b_layer3_configuration.vlan_id = AAZIntType(
                serialized_name="vlanId",
                flags={"required": True},
            )

            system_data = cls._schema_on_200.system_data
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

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_static_route_properties_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("nextHop", AAZListType, ".next_hop", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("prefix", AAZStrType, ".prefix", typ_kwargs={"flags": {"required": True}})

        next_hop = _builder.get(".nextHop")
        if next_hop is not None:
            next_hop.set_elements(AAZStrType, ".")

    _schema_static_route_properties_read = None

    @classmethod
    def _build_schema_static_route_properties_read(cls, _schema):
        if cls._schema_static_route_properties_read is not None:
            _schema.next_hop = cls._schema_static_route_properties_read.next_hop
            _schema.prefix = cls._schema_static_route_properties_read.prefix
            return

        cls._schema_static_route_properties_read = _schema_static_route_properties_read = AAZObjectType()

        static_route_properties_read = _schema_static_route_properties_read
        static_route_properties_read.next_hop = AAZListType(
            serialized_name="nextHop",
            flags={"required": True},
        )
        static_route_properties_read.prefix = AAZStrType(
            flags={"required": True},
        )

        next_hop = _schema_static_route_properties_read.next_hop
        next_hop.Element = AAZStrType()

        _schema.next_hop = cls._schema_static_route_properties_read.next_hop
        _schema.prefix = cls._schema_static_route_properties_read.prefix


__all__ = ["Update"]
