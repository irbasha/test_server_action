from common.methods import set_progress

from sst_custom_modules import sst_ansible_commons

from utilities.logger import ThreadLogger

logger = ThreadLogger('__name__')


def run(job, logger=None, **kwargs):
    resource = kwargs.get('resource')
    inventory_group_id = kwargs.get("inventory_group", "{{inventory_group}}")
    playbook_path = kwargs.get("playbook_path", "{{playbook_path}}")
    extra_vars = kwargs.get("extra_vars", "{{extra_vars}}")
    server_name_regex_filter = None
    timeout_as_string = kwargs.get("timeout", "{{script_timeout}}")

    return sst_ansible_commons.run_playbooks(
        current_job=job,
        playbook_paths=playbook_path,
        extra_vars=extra_vars,
        server_name_regex_filter=server_name_regex_filter,
        timeout_as_string=timeout_as_string,
        resource=resource
    )


def generate_options_for_inventory_group(profile=None, form_data=None, form_prefix=None, control_value=None, **kwargs):
    options = sst_ansible_commons.get_inventory_group_options()
    return options


def generate_options_for_playbook_path(profile=None, form_data=None, form_prefix=None, control_value=None, **kwargs):
    inventory_group_id = control_value
    if inventory_group_id:
        options = sst_ansible_commons.get_playbooks_options_for_inventory_group_id(
            inventory_group_id)
    else:
        options = sst_ansible_commons.get_all_playbook_options()
    return options
