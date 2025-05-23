# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from azext_confcom.os_util import load_json_from_file, load_str_from_file

# input json values
ACI_FIELD_VERSION = "version"
ACI_FIELD_RESOURCES = "resources"
ACI_FIELD_RESOURCES_NAME = "name"
ACI_FIELD_CONTAINERS = "containers"
ACI_FIELD_SCENARIO = "scenario"
ACI_FIELD_CONTAINERS_NAME = "name"
ACI_FIELD_CONTAINERS_CONTAINERIMAGE = "containerImage"
ACI_FIELD_CONTAINERS_ENVS = "environmentVariables"
ACI_FIELD_CONTAINERS_ENVS_NAME = "name"
ACI_FIELD_CONTAINERS_ENVS_VALUE = "value"
ACI_FIELD_CONTAINERS_ENVS_STRATEGY = "strategy"
ACI_FIELD_CONTAINERS_ENVS_REQUIRED = "required"
ACI_FIELD_CONTAINERS_COMMAND = "command"
ACI_FIELD_CONTAINERS_WORKINGDIR = "workingDir"
ACI_FIELD_CONTAINERS_MOUNTS = "mounts"
ACI_FIELD_CONTAINERS_MOUNTS_TYPE = "mountType"
ACI_FIELD_CONTAINERS_MOUNTS_PATH = "mountPath"
ACI_FIELD_CONTAINERS_MOUNTS_READONLY = "readonly"
ACI_FIELD_CONTAINERS_WAIT_MOUNT_POINTS = "wait_mount_points"
ACI_FIELD_CONTAINERS_ALLOW_ELEVATED = "allow_elevated"
ACI_FIELD_CONTAINERS_SECURITY_CONTEXT = "securityContext"
ACI_FIELD_CONTAINERS_ALLOW_PRIVILEGE_ESCALATION = "allowPrivilegeEscalation"
ACI_FIELD_CONTAINERS_RUN_AS_USER = "runAsUser"
ACI_FIELD_CONTAINERS_RUN_AS_GROUP = "runAsGroup"
ACI_FIELD_CONTAINERS_SECCOMP_PROFILE = "seccompProfile"
ACI_FIELD_CONTAINERS_REGO_FRAGMENTS = "fragments"
ACI_FIELD_CONTAINERS_REGO_FRAGMENTS_FEED = "feed"
ACI_FIELD_CONTAINERS_REGO_FRAGMENTS_ISS = "iss"
ACI_FIELD_CONTAINERS_REGO_FRAGMENTS_MINIMUM_SVN = "minimumSvn"
ACI_FIELD_CONTAINERS_REGO_FRAGMENTS_INCLUDES = "includes"
ACI_FIELD_CONTAINERS_ID = "id"
ACI_FIELD_CONTAINERS_CONFIGMAP = "configMap"
ACI_FIELD_CONTAINERS_CONFIGMAP_KEYVALUE = "keyValuePairs"

ACI_FIELD_CONTAINERS_ARCHITECTURE_KEY = "Architecture"
ACI_FIELD_CONTAINERS_ARCHITECTURE_VALUE = "amd64"


ACI_FIELD_CONTAINERS_EXEC_PROCESSES = "execProcesses"
ACI_FIELD_CONTAINERS_ALLOW_STDIO_ACCESS = "allowStdioAccess"
ACI_FIELD_CONTAINERS_LIVENESS_PROBE = "livenessProbe"
ACI_FIELD_CONTAINERS_READINESS_PROBE = "readinessProbe"
ACI_FIELD_CONTAINERS_PROBE_ACTION = "exec"
ACI_FIELD_CONTAINERS_PROBE_COMMAND = "command"
ACI_FIELD_CONTAINERS_SIGNAL_CONTAINER_PROCESSES = "signals"

ACI_FIELD_TEMPLATE_PROPERTIES = "properties"
ACI_FIELD_TEMPLATE_PARAMETERS = "parameters"
ACI_FIELD_TEMPLATE_CONTAINERS = "containers"
ACI_FIELD_TEMPLATE_INIT_CONTAINERS = "initContainers"
ACI_FIELD_TEMPLATE_VARIABLES = "variables"
ACI_FIELD_TEMPLATE_VOLUMES = "volumes"
ACI_FIELD_TEMPLATE_IMAGE = "image"
ACI_FIELD_TEMPLATE_SECURITY_CONTEXT = "securityContext"
ACI_FIELD_TEMPLATE_RESOURCE_LABEL = "Microsoft.ContainerInstance/containerGroups"
ACI_FIELD_TEMPLATE_RESOURCE_PROFILE_LABEL = "Microsoft.ContainerInstance/containerGroupProfiles"
ACI_FIELD_TEMPLATE_COMMAND = "command"
ACI_FIELD_TEMPLATE_ENTRYPOINT = "entrypoint"
ACI_FIELD_TEMPLATE_ENVS = "environmentVariables"
ACI_FIELD_TEMPLATE_VOLUME_MOUNTS = "volumeMounts"
ACI_FIELD_TEMPLATE_MOUNTS_TYPE = "mountType"
ACI_FIELD_TEMPLATE_MOUNTS_PATH = "mountPath"
ACI_FIELD_TEMPLATE_MOUNTS_READONLY = "readOnly"
ACI_FIELD_TEMPLATE_CONFCOM_PROPERTIES = "confidentialComputeProperties"
ACI_FIELD_TEMPLATE_CCE_POLICY = "ccePolicy"
ACI_FIELD_CONTAINERS_PRIVILEGED = "privileged"
ACI_FIELD_CONTAINERS_CAPABILITIES = "capabilities"
ACI_FIELD_CONTAINERS_CAPABILITIES_ADD = "add"
ACI_FIELD_CONTAINERS_CAPABILITIES_DROP = "drop"
ACI_FIELD_SUPPORTED_RESOURCES = [
    ACI_FIELD_TEMPLATE_RESOURCE_LABEL,
    ACI_FIELD_TEMPLATE_RESOURCE_PROFILE_LABEL
]
ACI_FIELD_TEMPLATE_TAGS = "tags"
ACI_FIELD_TEMPLATE_ZERO_SIDECAR = "Annotate-zero-sidecar"
ACI_FIELD_YAML_MOUNT_TYPE = "emptyDir"
ACI_FIELD_YAML_LIVENESS_PROBE = "livenessProbe"
ACI_FIELD_YAML_READINESS_PROBE = "readinessProbe"
ACI_FIELD_YAML_STARTUP_PROBE = "startupProbe"
ACI_FIELD_TEMPLATE_SPECIAL_ENV_VAR_REGEX_NAME = "THIM_ENDPOINT"
ACI_FIELD_TEMPLATE_SPECIAL_ENV_VAR_REGEX_VALUE = "^===CONFIDENTIAL.THIM.ENDPOINT===$"

VIRTUAL_NODE_YAML_METADATA = "metadata"
VIRTUAL_NODE_YAML_COMMAND = "command"
VIRTUAL_NODE_YAML_ARGS = "args"
VIRTUAL_NODE_YAML_NAME = "name"
VIRTUAL_NODE_YAML_ANNOTATIONS = "annotations"
VIRTUAL_NODE_YAML_LABELS = "labels"
VIRTUAL_NODE_YAML_LABEL_WORKLOAD_IDENTITY = "azure.workload.identity/use"
VIRTUAL_NODE_YAML_POLICY = "microsoft.containerinstance.virtualnode.ccepolicy"
VIRTUAL_NODE_YAML_LIFECYCLE = "lifecycle"
VIRTUAL_NODE_YAML_LIFECYCLE_POST_START = "postStart"
VIRTUAL_NODE_YAML_LIFECYCLE_PRE_STOP = "preStop"
VIRTUAL_NODE_YAML_LIFECYCLE_EXEC = "exec"
VIRTUAL_NODE_YAML_LIFECYCLE_COMMAND = "command"
VIRTUAL_NODE_YAML_RESOURCES = "resources"
VIRTUAL_NODE_YAML_RESOURCES_LIMITS = "limits"
VIRTUAL_NODE_YAML_RESOURCES_REQUESTS = "requests"
VIRTUAL_NODE_YAML_RESOURCES_CPU = "cpu"
VIRTUAL_NODE_YAML_RESOURCES_MEMORY = "memory"
VIRTUAL_NODE_YAML_RESOURCES_HUGEPAGES = "hugepages"
VIRTUAL_NODE_YAML_RESOURCES_EPHEMERAL_STORAGE = "ephemeral-storage"
VIRTUAL_NODE_YAML_SPECIAL_ENV_VAR_REGEX = "^===VIRTUALNODE2.CC.THIM.(.+)===$"
VIRTUAL_NODE_YAML_READ_ONLY_MANY = "ReadOnlyMany"

# output json values
POLICY_FIELD_CONTAINERS = "containers"
POLICY_FIELD_CONTAINERS_NAME = "name"
POLICY_FIELD_CONTAINERS_ID = "id"
POLICY_FIELD_CONTAINERS_ELEMENTS = "elements"
POLICY_FIELD_CONTAINERS_LENGTH = "length"
POLICY_FIELD_CONTAINERS_ELEMENTS_COMMANDS = "command"
POLICY_FIELD_CONTAINERS_ELEMENTS_ENVS = "env_rules"
POLICY_FIELD_CONTAINERS_ELEMENTS_ENVS_STRATEGY = "strategy"
POLICY_FIELD_CONTAINERS_ELEMENTS_ENVS_VALUE = "value"
POLICY_FIELD_CONTAINERS_ELEMENTS_ENVS_NAME = "name"
POLICY_FIELD_CONTAINERS_ELEMENTS_ENVS_RULE = "pattern"
POLICY_FIELD_CONTAINERS_ELEMENTS_REQUIRED = "required"
POLICY_FIELD_CONTAINERS_ELEMENTS_LAYERS = "layers"
POLICY_FIELD_CONTAINERS_ELEMENTS_WORKINGDIR = "working_dir"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS = "mounts"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_SOURCE = "source"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_DESTINATION = "destination"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_TYPE = "type"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_TYPE_BIND = "bind"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_OPTIONS = "options"
POLICY_FIELD_CONTAINERS_ELEMENTS_WAIT_MOUNT_POINTS = "wait_mount_points"
POLICY_FIELD_CONTAINERS_ELEMENTS_ALLOW_ELEVATED = "allow_elevated"
POLICY_FIELD_CONTAINERS_ELEMENTS_NO_NEW_PRIVILEGES = "no_new_privileges"
POLICY_FIELD_CONTAINERS_ELEMENTS_EXEC_PROCESSES = "exec_processes"
POLICY_FIELD_CONTAINERS_ELEMENTS_SIGNAL_CONTAINER_PROCESSES = "signals"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER = "user"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER_USER_IDNAME = "user_idname"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER_GROUP_IDNAMES = "group_idnames"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER_UMASK = "umask"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER_PATTERN = "pattern"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES = "capabilities"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES_BOUNDING = "bounding"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES_EFFECTIVE = "effective"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES_INHERITABLE = "inheritable"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES_PERMITTED = "permitted"
POLICY_FIELD_CONTAINERS_ELEMENTS_CAPABILITIES_AMBIENT = "ambient"
POLICY_FIELD_CONTAINERS_ELEMENTS_USER_STRATEGY = "strategy"
POLICY_FIELD_CONTAINERS_ELEMENTS_SECCOMP_PROFILE_SHA256 = "seccomp_profile_sha256"
POLICY_FIELD_CONTAINERS_ELEMENTS_ALLOW_STDIO_ACCESS = "allow_stdio_access"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS = "fragments"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_FEED = "feed"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_PATH = "path"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_ISS = "iss"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_ISSUER = "issuer"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_MINIMUM_SVN = "minimum_svn"
POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_INCLUDES = "includes"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_CONFIGMAP_LOCATION = "/mnt/configmap"
POLICY_FIELD_CONTAINERS_ELEMENTS_MOUNTS_CONFIGMAP_TYPE = "emptyDir"
REGO_CONTAINER_START = "containers := "
REGO_FRAGMENT_START = "fragments := "

# scenario options
VN2 = "vn2"
ACI = "aci"
KATA = "kata"


CONFIG_FILE = "./data/internal_config.json"

script_directory = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = f"{script_directory}/{CONFIG_FILE}"

_config = load_json_from_file(CONFIG_FILE_PATH)
DEFAULT_WORKING_DIR = _config["containerd"]["defaultWorkingDir"]

MOUNT_SOURCE_TABLE = {}
for entry in _config["mount"]["source_table"]:
    mount_type, mount_source = entry.get("mountType"), entry.get("source")
    MOUNT_SOURCE_TABLE[mount_type] = mount_source

BASELINE_SIDECAR_CONTAINERS = _config["sidecar_base_names"]
# OPENGCS environment variables for customer containers
OPENGCS_ENV_RULES = _config["openGCS"]["environmentVariables"]
# Fabric environment variables for customer containers
FABRIC_ENV_RULES = _config["fabric"]["environmentVariables"]
# Managed Identity environment variables for customer containers
MANAGED_IDENTITY_ENV_RULES = _config["managedIdentity"]["environmentVariables"]
# VN2 environment variables
VIRTUAL_NODE_ENV_RULES = _config["default_envs_virtual_node"]["environmentVariables"]
# VN2 environment variables for workload identities
VIRTUAL_NODE_ENV_RULES_WORKLOAD_IDENTITY = _config["workload_identity_virtual_node"]["environmentVariables"]
# Enable container restart environment variable for all containers
ENABLE_RESTART_ENV_RULE = _config["enableRestart"]["environmentVariables"]
# default mounts image for customer containers
DEFAULT_MOUNTS_USER = _config["mount"]["default_mounts_user"]
# default mounts used for VN2
DEFAULT_MOUNTS_USER_VIRTUAL_NODE = _config["mount"]["default_mounts_user_virtual_node"]
DEFAULT_MOUNTS_VIRTUAL_NODE = _config["mount"]["default_mounts_virtual_node"]
DEFAULT_MOUNTS_PRIVILEGED_VIRTUAL_NODE = _config["mount"]["default_mounts_virtual_node_privileged"]
DEFAULT_MOUNTS_WORKLOAD_IDENTITY_VIRTUAL_NODE = _config["mount"]["default_mounts_workload_identity_virtual_node"]
# default mounts policy options for all containers
DEFAULT_MOUNT_POLICY = _config["mount"]["default_policy"]
# default rego policy to be added to all user containers
DEFAULT_REGO_FRAGMENTS = _config["default_rego_fragments"]
# things that need to be set for debug mode
DEBUG_MODE_SETTINGS = _config["debugMode"]
# reserved fragment names for existing pieces of Rego
RESERVED_FRAGMENT_NAMES = _config["reserved_fragment_namespaces"]
# fragment artifact type
ARTIFACT_TYPE = "application/x-ms-ccepolicy-frag"
# customer rego file for data to be injected
REGO_FILE = "./data/customer_rego_policy.txt"
REGO_FRAGMENT_FILE = "./data/customer_rego_fragment.txt"
script_directory = os.path.dirname(os.path.realpath(__file__))
REGO_FILE_PATH = f"{script_directory}/{REGO_FILE}"
REGO_FRAGMENT_FILE_PATH = f"{script_directory}/{REGO_FRAGMENT_FILE}"
REGO_IMPORT_FILE_STRUCTURE = """
{
    "fragments": []
}
"""
CUSTOMER_REGO_POLICY = load_str_from_file(REGO_FILE_PATH)
CUSTOMER_REGO_FRAGMENT = load_str_from_file(REGO_FRAGMENT_FILE_PATH)
# sidecar rego file
SIDECAR_REGO_FILE = "./data/sidecar_rego_policy.txt"
SIDECAR_REGO_FILE_PATH = f"{script_directory}/{SIDECAR_REGO_FILE}"
SIDECAR_REGO_POLICY = load_str_from_file(SIDECAR_REGO_FILE_PATH)
# data folder
DATA_FOLDER = os.path.join(script_directory, "data")

# api version
API_VERSION = _config["version_api"]
# default containers to be added to all container groups
DEFAULT_CONTAINERS = _config["default_containers"]
# default container user config to be added for security context
DEFAULT_USER = _config["default_user"]
# default unpriviliged user capabilities to be added for security context
DEFAULT_UNPRIVILEGED_CAPABILITIES = _config["default_unprivileged_capabilities"]
# default priviliged user capabilities to be added for security context
DEFAULT_PRIVILEGED_CAPABILITIES = _config["default_privileged_capabilities"]
# these signals are hardcoded because the signals package in python is not portable across platforms
SIGNALS = {
    "SIGHUP": 1,
    "SIGINT": 2,
    "SIGQUIT": 3,
    "SIGILL": 4,
    "SIGTRAP": 5,
    "SIGABRT": 6,
    "SIGIOT": 6,
    "SIGBUS": 7,
    "SIGFPE": 8,
    "SIGKILL": 9,
    "SIGUSR1": 10,
    "SIGSEGV": 11,
    "SIGUSR2": 12,
    "SIGPIPE": 13,
    "SIGALRM": 14,
    "SIGTERM": 15,
    "SIGSTKFLT": 16,
    "SIGCHLD": 17,
    "SIGCONT": 18,
    "SIGSTOP": 19,
    "SIGTSTP": 20,
    "SIGTTIN": 21,
    "SIGTTOU": 22,
    "SIGURG": 23,
    "SIGXCPU": 24,
    "SIGXFSZ": 25,
    "SIGVTALRM": 26,
    "SIGPROF": 27,
    "SIGWINCH": 28,
    "SIGIO": 29,
    "SIGPWR": 30,
    "SIGSYS": 31,
    "SIGUNUSED": 31
}
# these algorithms are the only supported ones in https://github.com/veraison/go-cose/blob/main/algorithm.go
SUPPORTED_ALGOS = [
    "PS256",
    "PS384",
    "PS512",
    "ES256",
    "ES384",
    "ES512",
    "EdDSA",
]
