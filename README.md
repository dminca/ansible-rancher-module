# ansible-rancher-module
Module for communicating with Rancher API

## Description
The need to communicate with Rancher API arose. After launching the Rancher Server container, Rancher Agents must be registered, the Environments must be created, Access Control must be configured.

That's why this module has been created, to satisfy those and many more requirements, in order to provision Rancher clusters very fast.

## Prerequisites
To test this module, you need a [running rancher server][6] that listens on port
`8080`. You can achieve that by running:

```sh
docker run --rm -p 8080:8080 rancher/server
```

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
- [PyFormat - using % and .format() for great good][3]
- [Python programming wiki][4]
- [requests python library documentation][5]

[1]: https://github.com/loopingz/ansible-rancher-module
[2]: https://jsonformatter.org
[3]: https://pyformat.info
[4]: https://en.wikibooks.org/wiki/Python_Programming
[5]: http://docs.python-requests.org/en/master/
[6]: http://rancher.com/docs/rancher/latest/en/installing-rancher/installing-server/#launching-rancher-server---single-container-non-ha
