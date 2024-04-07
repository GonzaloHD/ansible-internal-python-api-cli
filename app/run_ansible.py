import os
from app import config
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
import logging


def run_ansible_playbook(
                         playbook_path,
                         tags=None,
                         extra_vars=None,
                         inventory_file=None,
                         limit=None):

    try:

        loader = DataLoader()
        inventory = InventoryManager(loader=loader, sources=[os.path.abspath(inventory_file)])
        variable_manager = VariableManager(loader=loader, inventory=inventory)
        context.CLIARGS = ImmutableDict(
            become=True, 
            become_method="sudo", 
            become_user="root", 
            ansible_user= 'ubuntu',
            tags=tags,
            connection='ssh', 
            # connection='smart', 
            # connection = 'winrm',
            ansible_winrm_server_cert_validation='ignore',
            verbosity=2,
            forks=10,
            check=False,
            syntax=None,  # Define syntax key here
            start_at_task=None
            )

        playbook_executor = PlaybookExecutor(playbooks=[playbook_path],
                                             inventory=inventory,
                                             variable_manager=variable_manager,
                                             loader=loader,
                                             passwords={})
        # Set stdout callback for the task queue manager (tqm)
        playbook_executor._tqm._stdout_callback = 'default'

        # Set playbook tags, extra variables, and limit
        # playbook_executor._tqm._tags = tags
        playbook_executor._tqm._extra_vars = extra_vars
        if limit:
            playbook_executor._tqm._inventory.set_subset(limit)

        # Run the playbook
        playbook_executor.run()

        logging.info("Ansible playbook executed successfully.")

    except Exception as e:
        logging.error(e, exc_info=True)


if __name__ == "__main__":

    playbook_directory = f"{config['cli'].get('root_directory')}"
    tags = {}   
    # extra_vars = {"single_site": "ansible-dev.gonzalohd.xyz"}
    inventory_file = f"{playbook_directory}/hosts"
    playbook_path = f"{playbook_directory}/playbook.yml"
    ansible_cfg_file = f"{playbook_directory}/ansible.cfg"
    # limit = "my_host_or_group"
    # Construct the playbook executor with ansible.cfg
    os.environ['ANSIBLE_CONFIG'] = ansible_cfg_file
    run_ansible_playbook(playbook_path=playbook_path, inventory_file=inventory_file, tags=tags)
