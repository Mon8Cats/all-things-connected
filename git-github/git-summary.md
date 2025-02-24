# Git Summary

## Generate SSH key

```bash
# ed25519 a twisted Edwards curve: a kind of elliptic curve 
ssh-keygen -t ed25519 -C "myemail@example.com"

# legacy system
ssh-keygen -t rsa -b 4096 -C "myemail@example.com"

# start SSH Agent
eval "$(ssh-agent -s)"

# verify if file exists
open ~/.ssh/config

# create file if doesn't exists
touch ~/.ssh/config

# open config file
vi ~/.ssh/config

Host stric github.com
	User git
	HostName ssh.github.com
	PreferredAuthentications publickey
	IdentityFile ~/.ssh/id_ed25519_stric
	Port 443
	
Host bedside github.com
	User git
	HostName ssh.github.com
	PreferredAuthentications publickey
	IdentityFile ~/.ssh/id_ed25519_bedside
	Port 443

known_hosts 

```

## Add a new SSH key to my GitHub account

```bash
# copy the content from the public key file
cat $HOME/.ssh/id_ed25519.pub

# go to GitHub/ settings/ SSH and GPG keys/ new SSH key
# give a title and copy the content.

# verify
ssh -T git@github.com
# Hi SteveKimMHS! You've successfully authenticated, but GitHub does not provide shell access.

```
