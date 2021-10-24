# Raspberry Home Setup

## Ansible provisioning
Installation Requirements
```
# local
$ touch /Volumes/boot/ssh
$ ansible-galaxy install -r requirements.yml
ssh-copy-id -i ~/.ssh/id_ed25519.pub pi@192.168.1.57

# remote
$ apt-get install python3
```
