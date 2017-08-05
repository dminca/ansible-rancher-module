# ansible-rancher-module
Module for communicating with Rancher API

## Description
The need to communicate with Rancher API arose. After launching the Rancher Server container, Rancher Agents must be registered, the Environments must be created, Access Control must be configured.

That's why this module has been created, to satisfy those and many more requirements, in order to provision Rancher clusters very fast.

## Running the playbook
> Before running the playbook, requirements must be installed.

```sh
ansible-galaxy install -r requirements.yml
```

> After installing requirements, proceed to run the playbook

```sh
ansible-playbook playbook.yml
```

## Resources

- [Ansible Rancher Module by loopingz][1]
- [JSONformatted tool][2]

[1]: https://github.com/loopingz/ansible-rancher-module
[2]: https://jsonformatter.org