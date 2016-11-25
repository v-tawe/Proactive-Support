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

from .resource import Resource


class HostingEnvironment(Resource):
    """Description of an hostingEnvironment (App Service Environment).

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param hosting_environment_name: Name of the hostingEnvironment (App
     Service Environment)
    :type hosting_environment_name: str
    :param hosting_environment_location: Location of the hostingEnvironment
     (App Service Environment), e.g. "West US"
    :type hosting_environment_location: str
    :param provisioning_state: Provisioning state of the hostingEnvironment
     (App Service Environment). Possible values include: 'Succeeded',
     'Failed', 'Canceled', 'InProgress', 'Deleting'
    :type provisioning_state: str or :class:`ProvisioningState
     <azure.mgmt.web.models.ProvisioningState>`
    :param status: Current status of the hostingEnvironment (App Service
     Environment). Possible values include: 'Preparing', 'Ready', 'Scaling',
     'Deleting'
    :type status: str or :class:`HostingEnvironmentStatus
     <azure.mgmt.web.models.HostingEnvironmentStatus>`
    :param vnet_name: Name of the hostingEnvironment's (App Service
     Environment) virtual network
    :type vnet_name: str
    :param vnet_resource_group_name: Resource group of the
     hostingEnvironment's (App Service Environment) virtual network
    :type vnet_resource_group_name: str
    :param vnet_subnet_name: Subnet of the hostingEnvironment's (App Service
     Environment) virtual network
    :type vnet_subnet_name: str
    :param virtual_network: Description of the hostingEnvironment's (App
     Service Environment) virtual network
    :type virtual_network: :class:`VirtualNetworkProfile
     <azure.mgmt.web.models.VirtualNetworkProfile>`
    :param internal_load_balancing_mode: Specifies which endpoints to serve
     internally in the hostingEnvironment's (App Service Environment) VNET.
     Possible values include: 'None', 'Web', 'Publishing'
    :type internal_load_balancing_mode: str or
     :class:`InternalLoadBalancingMode
     <azure.mgmt.web.models.InternalLoadBalancingMode>`
    :param multi_size: Front-end VM size, e.g. "Medium", "Large"
    :type multi_size: str
    :param multi_role_count: Number of front-end instances
    :type multi_role_count: int
    :param worker_pools: Description of worker pools with worker size ids, VM
     sizes, and number of workers in each pool
    :type worker_pools: list of :class:`WorkerPool
     <azure.mgmt.web.models.WorkerPool>`
    :param ipssl_address_count: Number of IP SSL addresses reserved for this
     hostingEnvironment (App Service Environment)
    :type ipssl_address_count: int
    :param database_edition: Edition of the metadata database for the
     hostingEnvironment (App Service Environment) e.g. "Standard"
    :type database_edition: str
    :param database_service_objective: Service objective of the metadata
     database for the hostingEnvironment (App Service Environment) e.g. "S0"
    :type database_service_objective: str
    :param upgrade_domains: Number of upgrade domains of this
     hostingEnvironment (App Service Environment)
    :type upgrade_domains: int
    :param subscription_id: Subscription of the hostingEnvironment (App
     Service Environment)
    :type subscription_id: str
    :param dns_suffix: DNS suffix of the hostingEnvironment (App Service
     Environment)
    :type dns_suffix: str
    :param last_action: Last deployment action on this hostingEnvironment
     (App Service Environment)
    :type last_action: str
    :param last_action_result: Result of the last deployment action on this
     hostingEnvironment (App Service Environment)
    :type last_action_result: str
    :param allowed_multi_sizes: List of comma separated strings describing
     which VM sizes are allowed for front-ends
    :type allowed_multi_sizes: str
    :param allowed_worker_sizes: List of comma separated strings describing
     which VM sizes are allowed for workers
    :type allowed_worker_sizes: str
    :param maximum_number_of_machines: Maximum number of VMs in this
     hostingEnvironment (App Service Environment)
    :type maximum_number_of_machines: int
    :param vip_mappings: Description of IP SSL mapping for this
     hostingEnvironment (App Service Environment)
    :type vip_mappings: list of :class:`VirtualIPMapping
     <azure.mgmt.web.models.VirtualIPMapping>`
    :param environment_capacities: Current total, used, and available worker
     capacities
    :type environment_capacities: list of :class:`StampCapacity
     <azure.mgmt.web.models.StampCapacity>`
    :param network_access_control_list: Access control list for controlling
     traffic to the hostingEnvironment (App Service Environment)
    :type network_access_control_list: list of
     :class:`NetworkAccessControlEntry
     <azure.mgmt.web.models.NetworkAccessControlEntry>`
    :param environment_is_healthy: True/false indicating whether the
     hostingEnvironment (App Service Environment) is healthy
    :type environment_is_healthy: bool
    :param environment_status: Detailed message about with results of the
     last check of the hostingEnvironment (App Service Environment)
    :type environment_status: str
    :param resource_group: Resource group of the hostingEnvironment (App
     Service Environment)
    :type resource_group: str
    :param api_management_account_id: Api Management Account associated with
     this Hosting Environment
    :type api_management_account_id: str
    :param suspended: True/false indicating whether the hostingEnvironment is
     suspended. The environment can be suspended e.g. when the management
     endpoint is no longer available
     (most likely because NSG blocked the incoming traffic)
    :type suspended: bool
    :param cluster_settings: Custom settings for changing the behavior of the
     hosting environment
    :type cluster_settings: list of :class:`NameValuePair
     <azure.mgmt.web.models.NameValuePair>`
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'hosting_environment_name': {'key': 'properties.name', 'type': 'str'},
        'hosting_environment_location': {'key': 'properties.location', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
        'status': {'key': 'properties.status', 'type': 'HostingEnvironmentStatus'},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str'},
        'vnet_resource_group_name': {'key': 'properties.vnetResourceGroupName', 'type': 'str'},
        'vnet_subnet_name': {'key': 'properties.vnetSubnetName', 'type': 'str'},
        'virtual_network': {'key': 'properties.virtualNetwork', 'type': 'VirtualNetworkProfile'},
        'internal_load_balancing_mode': {'key': 'properties.internalLoadBalancingMode', 'type': 'InternalLoadBalancingMode'},
        'multi_size': {'key': 'properties.multiSize', 'type': 'str'},
        'multi_role_count': {'key': 'properties.multiRoleCount', 'type': 'int'},
        'worker_pools': {'key': 'properties.workerPools', 'type': '[WorkerPool]'},
        'ipssl_address_count': {'key': 'properties.ipsslAddressCount', 'type': 'int'},
        'database_edition': {'key': 'properties.databaseEdition', 'type': 'str'},
        'database_service_objective': {'key': 'properties.databaseServiceObjective', 'type': 'str'},
        'upgrade_domains': {'key': 'properties.upgradeDomains', 'type': 'int'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'dns_suffix': {'key': 'properties.dnsSuffix', 'type': 'str'},
        'last_action': {'key': 'properties.lastAction', 'type': 'str'},
        'last_action_result': {'key': 'properties.lastActionResult', 'type': 'str'},
        'allowed_multi_sizes': {'key': 'properties.allowedMultiSizes', 'type': 'str'},
        'allowed_worker_sizes': {'key': 'properties.allowedWorkerSizes', 'type': 'str'},
        'maximum_number_of_machines': {'key': 'properties.maximumNumberOfMachines', 'type': 'int'},
        'vip_mappings': {'key': 'properties.vipMappings', 'type': '[VirtualIPMapping]'},
        'environment_capacities': {'key': 'properties.environmentCapacities', 'type': '[StampCapacity]'},
        'network_access_control_list': {'key': 'properties.networkAccessControlList', 'type': '[NetworkAccessControlEntry]'},
        'environment_is_healthy': {'key': 'properties.environmentIsHealthy', 'type': 'bool'},
        'environment_status': {'key': 'properties.environmentStatus', 'type': 'str'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'api_management_account_id': {'key': 'properties.apiManagementAccountId', 'type': 'str'},
        'suspended': {'key': 'properties.suspended', 'type': 'bool'},
        'cluster_settings': {'key': 'properties.clusterSettings', 'type': '[NameValuePair]'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, hosting_environment_name=None, hosting_environment_location=None, provisioning_state=None, status=None, vnet_name=None, vnet_resource_group_name=None, vnet_subnet_name=None, virtual_network=None, internal_load_balancing_mode=None, multi_size=None, multi_role_count=None, worker_pools=None, ipssl_address_count=None, database_edition=None, database_service_objective=None, upgrade_domains=None, subscription_id=None, dns_suffix=None, last_action=None, last_action_result=None, allowed_multi_sizes=None, allowed_worker_sizes=None, maximum_number_of_machines=None, vip_mappings=None, environment_capacities=None, network_access_control_list=None, environment_is_healthy=None, environment_status=None, resource_group=None, api_management_account_id=None, suspended=None, cluster_settings=None):
        super(HostingEnvironment, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.hosting_environment_name = hosting_environment_name
        self.hosting_environment_location = hosting_environment_location
        self.provisioning_state = provisioning_state
        self.status = status
        self.vnet_name = vnet_name
        self.vnet_resource_group_name = vnet_resource_group_name
        self.vnet_subnet_name = vnet_subnet_name
        self.virtual_network = virtual_network
        self.internal_load_balancing_mode = internal_load_balancing_mode
        self.multi_size = multi_size
        self.multi_role_count = multi_role_count
        self.worker_pools = worker_pools
        self.ipssl_address_count = ipssl_address_count
        self.database_edition = database_edition
        self.database_service_objective = database_service_objective
        self.upgrade_domains = upgrade_domains
        self.subscription_id = subscription_id
        self.dns_suffix = dns_suffix
        self.last_action = last_action
        self.last_action_result = last_action_result
        self.allowed_multi_sizes = allowed_multi_sizes
        self.allowed_worker_sizes = allowed_worker_sizes
        self.maximum_number_of_machines = maximum_number_of_machines
        self.vip_mappings = vip_mappings
        self.environment_capacities = environment_capacities
        self.network_access_control_list = network_access_control_list
        self.environment_is_healthy = environment_is_healthy
        self.environment_status = environment_status
        self.resource_group = resource_group
        self.api_management_account_id = api_management_account_id
        self.suspended = suspended
        self.cluster_settings = cluster_settings
