# ansible-internal-python-api-cli

Run ansible playbook with roles using Ansible Internal Python API

## Internal Python API:

This API provides programmatic access to Ansible functionalities.
While it might seem convenient, it's not officially documented or supported by the Ansible team.
Drawbacks of Internal API:

Changes without notice: Ansible developers might modify the internal API in future releases, potentially breaking your code.
Limited documentation: Finding official documentation or support for the internal API is difficult.
Unforeseen issues: You might encounter unexpected behavior due to unsupported features or changes within the API.
Alternatives to Consider:

ansible-runner: This is an officially supported Python library specifically designed for running Ansible playbooks. It offers better documentation and is considered the preferred method for programmatic execution. Here's the documentation: https://github.com/ansible/ansible-runner.
ansible module (CLI): You can also leverage the ansible command-line tool directly from your Python code using subprocess or similar libraries. This provides a more structured approach than directly using the internal API.
Current Status (as of April 7, 2024):

While there hasn't been a major shift in Ansible's official stance on the internal API, the development of ansible-runner signifies their commitment to providing a stable and supported solution for programmatic Ansible execution.

## Recommendation:

For most cases, using ansible-runner is the most reliable and recommended approach. It offers a well-documented and supported interface for running Ansible playbooks from your Python applications.
