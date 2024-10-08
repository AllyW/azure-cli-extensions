# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import *
import time


class FabricScenario(ScenarioTest):
    @ResourceGroupPreparer(parameter_name_for_location='resource_group_location')
    def test_fabric_capacity(self, resource_group, resource_group_location):
        display_name = self.create_random_name(prefix='cli-', length=30)
        self.kwargs.update({
            'name': self.create_random_name(prefix='cli', length=24),
            'loc': resource_group_location,
            'display_name': display_name,
            'identifier_uri': f'api://{display_name}'
        })
        appId = self.cmd('az ad app create --display-name {display_name} --identifier-uris {identifier_uri}').get_output_in_json()['appId']
        self.kwargs.update({'app_id': appId})
        spId = self.cmd('az ad sp create --id {app_id}').get_output_in_json()['id']
        self.kwargs.update({'administrator': spId})
        time.sleep(60)

        self.cmd('az fabric capacity create --resource-group {rg} --name {name} --sku name="F2" '
                 '--location {loc} --sku tier="Fabric" --administration members[0]="{administrator}" --no-wait')

        self.cmd('az fabric capacity wait --resource-group {rg} --name {name} --created')

        self.cmd('az fabric capacity list --resource-group {rg}',
                 checks=[
                     self.check('length(@)', 1),
                 ])

        self.cmd('az fabric capacity show -g {rg} --name {name}',
                 checks=[
                     self.check('provisioningState', 'Succeeded'),
                     self.check('name', '{name}'),
                     self.check('sku.name', 'F2'),
                     self.check('sku.tier', 'Fabric'),
                     self.check('administration.members[0]', self.kwargs['administrator']),
                 ])

        self.cmd('az fabric capacity update --resource-group {rg} --name {name} --sku name="F4"',
                 checks=[
                     self.check('name', '{name}'),
                     self.check('sku.name', 'F4'),
                 ])

        self.cmd('az fabric capacity show -g {rg} -n {name}',
                 checks=[
                     self.check('name', '{name}'),
                     self.check('sku.name', 'F4'),
                 ])

        self.cmd('az fabric capacity delete -g {rg} -n {name} -y')

        self.cmd('az fabric capacity list -g {rg}',
                 checks=[
                     self.check('length(@)', 0)])
        
        self.cmd('az ad app delete --id {app_id}')
