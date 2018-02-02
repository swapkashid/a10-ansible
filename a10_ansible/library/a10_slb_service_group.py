#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = """
module: a10_slb_service_group
description:
    - None
short_description: Configures A10 slb.service-group
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
        - present
        - absent
        required: True
    a10_host:
        description:
        - Host for AXAPI authentication
        required: True
    a10_username:
        description:
        - Username for AXAPI authentication
        required: True
    a10_password:
        description:
        - Password for AXAPI authentication
        required: True
    name:
        description:
        - "None"
        required: True
    protocol:
        description:
        - "None"
        required: False
    template_port:
        description:
        - "None"
        required: False
    template_server:
        description:
        - "None"
        required: False
    template_policy:
        description:
        - "None"
        required: False
    lb_method:
        description:
        - "None"
        required: False
    lc_method:
        description:
        - "None"
        required: False
    stateless_lb_method:
        description:
        - "None"
        required: False
    pseudo_round_robin:
        description:
        - "None"
        required: False
    stateless_auto_switch:
        description:
        - "None"
        required: False
    stateless_lb_method2:
        description:
        - "None"
        required: False
    conn_rate:
        description:
        - "None"
        required: False
    conn_rate_duration:
        description:
        - "None"
        required: False
    conn_revert_rate:
        description:
        - "None"
        required: False
    conn_rate_revert_duration:
        description:
        - "None"
        required: False
    conn_rate_grace_period:
        description:
        - "None"
        required: False
    conn_rate_log:
        description:
        - "None"
        required: False
    l4_session_usage:
        description:
        - "None"
        required: False
    l4_session_usage_duration:
        description:
        - "None"
        required: False
    l4_session_usage_revert_rate:
        description:
        - "None"
        required: False
    l4_session_revert_duration:
        description:
        - "None"
        required: False
    l4_session_usage_grace_period:
        description:
        - "None"
        required: False
    l4_session_usage_log:
        description:
        - "None"
        required: False
    min_active_member:
        description:
        - "None"
        required: False
    min_active_member_action:
        description:
        - "None"
        required: False
    reset_on_server_selection_fail:
        description:
        - "None"
        required: False
    priority_affinity:
        description:
        - "None"
        required: False
    reset_priority_affinity:
        description:
        - "None"
        required: False
    backup_server_event_log:
        description:
        - "None"
        required: False
    strict_select:
        description:
        - "None"
        required: False
    stats_data_action:
        description:
        - "None"
        required: False
    extended_stats:
        description:
        - "None"
        required: False
    traffic_replication_mirror:
        description:
        - "None"
        required: False
    traffic_replication_mirror_da_repl:
        description:
        - "None"
        required: False
    traffic_replication_mirror_ip_repl:
        description:
        - "None"
        required: False
    traffic_replication_mirror_sa_da_repl:
        description:
        - "None"
        required: False
    traffic_replication_mirror_sa_repl:
        description:
        - "None"
        required: False
    health_check:
        description:
        - "None"
        required: False
    health_check_disable:
        description:
        - "None"
        required: False
    priorities:
        description:
        - "Field priorities"
        required: False
        suboptions:
            priority:
                description:
                - "None"
            priority_action:
                description:
                - "None"
    sample_rsp_time:
        description:
        - "None"
        required: False
    rpt_ext_server:
        description:
        - "None"
        required: False
    report_delay:
        description:
        - "None"
        required: False
    top_slowest:
        description:
        - "None"
        required: False
    top_fastest:
        description:
        - "None"
        required: False
    uuid:
        description:
        - "None"
        required: False
    user_tag:
        description:
        - "None"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "None"
    reset:
        description:
        - "Field reset"
        required: False
        suboptions:
            auto_switch:
                description:
                - "None"
    member_list:
        description:
        - "Field member_list"
        required: False
        suboptions:
            name:
                description:
                - "None"
            port:
                description:
                - "None"
            fqdn_name:
                description:
                - "None"
            host:
                description:
                - "None"
            server_ipv6_addr:
                description:
                - "None"
            member_state:
                description:
                - "None"
            member_stats_data_disable:
                description:
                - "None"
            member_template:
                description:
                - "None"
            member_priority:
                description:
                - "None"
            uuid:
                description:
                - "None"
            user_tag:
                description:
                - "None"
            sampling_enable:
                description:
                - "Field sampling_enable"


"""

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["backup_server_event_log","conn_rate","conn_rate_duration","conn_rate_grace_period","conn_rate_log","conn_rate_revert_duration","conn_revert_rate","extended_stats","health_check","health_check_disable","l4_session_revert_duration","l4_session_usage","l4_session_usage_duration","l4_session_usage_grace_period","l4_session_usage_log","l4_session_usage_revert_rate","lb_method","lc_method","member_list","min_active_member","min_active_member_action","name","priorities","priority_affinity","protocol","pseudo_round_robin","report_delay","reset","reset_on_server_selection_fail","reset_priority_affinity","rpt_ext_server","sample_rsp_time","sampling_enable","stateless_auto_switch","stateless_lb_method","stateless_lb_method2","stats_data_action","strict_select","template_policy","template_port","template_server","top_fastest","top_slowest","traffic_replication_mirror","traffic_replication_mirror_da_repl","traffic_replication_mirror_ip_repl","traffic_replication_mirror_sa_da_repl","traffic_replication_mirror_sa_repl","user_tag","uuid",]

# our imports go at the top so we fail fast.
try:
    from a10_ansible import errors as a10_ex
    from a10_ansible.axapi_http import client_factory
    from a10_ansible.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=["present", "absent"])
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        name=dict(type='str',required=True,),
        protocol=dict(type='str',choices=['tcp','udp']),
        template_port=dict(type='str',),
        template_server=dict(type='str',),
        template_policy=dict(type='str',),
        lb_method=dict(type='str',choices=['dst-ip-hash','dst-ip-only-hash','fastest-response','least-request','src-ip-hash','src-ip-only-hash','weighted-rr','round-robin','round-robin-strict','odd-even-hash']),
        lc_method=dict(type='str',choices=['least-connection','service-least-connection','weighted-least-connection','service-weighted-least-connection']),
        stateless_lb_method=dict(type='str',choices=['stateless-dst-ip-hash','stateless-per-pkt-round-robin','stateless-src-dst-ip-hash','stateless-src-dst-ip-only-hash','stateless-src-ip-hash','stateless-src-ip-only-hash']),
        pseudo_round_robin=dict(type='bool',),
        stateless_auto_switch=dict(type='bool',),
        stateless_lb_method2=dict(type='str',choices=['stateless-dst-ip-hash','stateless-per-pkt-round-robin','stateless-src-dst-ip-hash','stateless-src-dst-ip-only-hash','stateless-src-ip-hash','stateless-src-ip-only-hash']),
        conn_rate=dict(type='int',),
        conn_rate_duration=dict(type='int',),
        conn_revert_rate=dict(type='int',),
        conn_rate_revert_duration=dict(type='int',),
        conn_rate_grace_period=dict(type='int',),
        conn_rate_log=dict(type='bool',),
        l4_session_usage=dict(type='int',),
        l4_session_usage_duration=dict(type='int',),
        l4_session_usage_revert_rate=dict(type='int',),
        l4_session_revert_duration=dict(type='int',),
        l4_session_usage_grace_period=dict(type='int',),
        l4_session_usage_log=dict(type='bool',),
        min_active_member=dict(type='int',),
        min_active_member_action=dict(type='str',choices=['dynamic-priority','skip-pri-set']),
        reset_on_server_selection_fail=dict(type='bool',),
        priority_affinity=dict(type='bool',),
        reset_priority_affinity=dict(type='bool',),
        backup_server_event_log=dict(type='bool',),
        strict_select=dict(type='bool',),
        stats_data_action=dict(type='str',choices=['stats-data-enable','stats-data-disable']),
        extended_stats=dict(type='bool',),
        traffic_replication_mirror=dict(type='bool',),
        traffic_replication_mirror_da_repl=dict(type='bool',),
        traffic_replication_mirror_ip_repl=dict(type='bool',),
        traffic_replication_mirror_sa_da_repl=dict(type='bool',),
        traffic_replication_mirror_sa_repl=dict(type='bool',),
        health_check=dict(type='str',),
        health_check_disable=dict(type='bool',),
        priorities=dict(type='list',priority=dict(type='int',),priority_action=dict(type='str',choices=['drop','drop-if-exceed-limit','proceed','reset','reset-if-exceed-limit'])),
        sample_rsp_time=dict(type='bool',),
        rpt_ext_server=dict(type='bool',),
        report_delay=dict(type='int',),
        top_slowest=dict(type='bool',),
        top_fastest=dict(type='bool',),
        uuid=dict(type='str',),
        user_tag=dict(type='str',),
        sampling_enable=dict(type='list',counters1=dict(type='str',choices=['all','server_selection_fail_drop','server_selection_fail_reset','service_peak_conn','service_healthy_host','service_unhealthy_host','service_req_count','service_resp_count','service_resp_2xx','service_resp_3xx','service_resp_4xx','service_resp_5xx'])),
        reset=dict(type='dict',auto_switch=dict(type='bool',)),
        member_list=dict(type='list',name=dict(type='str',required=True,),port=dict(type='int',required=True,),fqdn_name=dict(type='str',),host=dict(type='str',),server_ipv6_addr=dict(type='str',),member_state=dict(type='str',choices=['enable','disable','disable-with-health-check']),member_stats_data_disable=dict(type='bool',),member_template=dict(type='str',),member_priority=dict(type='int',),uuid=dict(type='str',),user_tag=dict(type='str',),sampling_enable=dict(type='list',counters1=dict(type='str',choices=['all','total_fwd_bytes','total_fwd_pkts','total_rev_bytes','total_rev_pkts','total_conn','total_rev_pkts_inspected','total_rev_pkts_inspected_status_code_2xx','total_rev_pkts_inspected_status_code_non_5xx','curr_req','total_req','total_req_succ','peak_conn','response_time','fastest_rsp_time','slowest_rsp_time','curr_ssl_conn','total_ssl_conn'])))
    ))

    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/service-group/{name}"
    f_dict = {}
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/service-group/{name}"
    f_dict = {}
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def build_envelope(title, data):
    return {
        title: data
    }

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        if isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            if isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def exists(module):
    try:
        module.client.get(existing_url(module))
        return True
    except a10_ex.NotFound:
        return False

def create(module, result):
    payload = build_json("service-group", module)
    try:
        post_result = module.client.post(new_url(module), payload)
        result.update(**post_result)
        result["changed"] = True
    except a10_ex.Exists:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result):
    payload = build_json("service-group", module)
    try:
        post_result = module.client.put(existing_url(module), payload)
        result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result):
    if not exists(module):
        return create(module, result)
    else:
        return update(module, result)

def absent(module, result):
    return delete(module, result)

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message=""
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    # TODO(remove hardcoded port #)
    a10_port = 443
    a10_protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        map(run_errors.append, validation_errors)
    
    if not valid:
        result["messages"] = "Validation failure"
        err_msg = "\n".join(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)

    if state == 'present':
        result = present(module, result)
    elif state == 'absent':
        result = absent(module, result)
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec())
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()