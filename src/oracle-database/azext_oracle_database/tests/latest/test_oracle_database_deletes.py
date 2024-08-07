# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------
import os
import unittest
import time

from azure.cli.testsdk.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

class OracleDatabaseDeleteScenario(ScenarioTest):
    @AllowLargeResponse(size_kb=10240)
    @ResourceGroupPreparer(name_prefix='cli_test_odba_rg')
    def test_oracledatabase_exadata_deletes(self, resource_group):
        subscription_id = self.get_subscription_id()
        self.kwargs.update({
            'infra_name': 'OFake_Infra_AzCLI',
            'location': 'eastus',
            'shape': 'Exadata.X9M',
            'tags': '{tagk1:tagv1}'
        })
        self.cmd('az oracle-database cloud-exadata-infrastructure delete '
                         '--resource-group ObsTestingFra '
                         '--name OFake_ppratees_0216_2 '
                         '--no-wait '
                         '--yes ')
        self.cmd('az oracle-database cloud-vm-cluster show '
                                 '--resource-group SDKTestRG '
                                 '--name OFakeVmTestA ')
        self.cmd('az oracle-database cloud-vm-cluster list '
                                 '--resource-group SDKTestRG ')
        self.cmd('az oracle-database cloud-vm-cluster delete '
                         '--resource-group SDKTestRG '
                         '--name OFakeVmTestA '
                         '--no-wait '
                         '--yes ')