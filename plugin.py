#!/bin/env python

from common.methods import set_progress

from sst_custom_modules import sst_ansible_commons

from utilities.logger import ThreadLogger

logger = ThreadLogger('__name__')


def run(job, logger=None, **kwargs):

	# Fetch playbook and timeout from kwargs, but default to action inputs.
	# This allows this action to be called both as .run_as_job() and as a server action.
	inventory_group_id = kwargs.get("inventory_group", "{{inventory_group}}")
	playbook_path = kwargs.get("playbook_path", "{{playbook_path}}")
	extra_vars = kwargs.get("extra_vars", """{{extra_vars}}""")
	server_name_regex_filter = kwargs.get("server_name_regex_filter", "{{server_name_regex_filter}}")
	timeout_as_string = kwargs.get("timeout", "{{script_timeout}}")

	return sst_ansible_commons.run(job, inventory_group_id, playbook_path, extra_vars, server_name_regex_filter, timeout_as_string, kwargs.get('resource'))

def generate_options_for_inventory_group(profile=None, form_data=None, form_prefix=None, control_value=None, **kwargs):
	return sst_ansible_commons.get_inventory_group_options()

def generate_options_for_playbook_path(profile=None, form_data=None, form_prefix=None, control_value=None, **kwargs):
	inventory_group_id = control_value
	return sst_ansible_commons.get_playbooks_options_for_inventory_group_id(inventory_group_id)
