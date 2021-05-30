# Set linux editing mode
set -o emacs

# pic-tools
eval $(ssh-agent); pic-tunnel-ingress-proxies 

# console
alias lkcv1='eval "$(ssh-agent)";  ssh-add -s /usr/lib/libykcs11.so'
alias lkcv2='eval "$(ssh-agent -s)"; ssh-add -s /usr/lib/libykcs11.so'

# git

Delete a branch
------------------
remote
git push origin --delete rkisnah/alarmfixes

local
git branch -d feature/login


## Create a branch
git checkout -b rkisnah/alarmfixes

## Minimize all windows
Ctrl Super D

# restart gui ubuntu
sudo systemctl restart systemd-logind
sudo systemctl restart gdm

# unix timestamps to UTC 
date -u -d @1571249945


# date
https://www.howtogeek.com/410442/how-to-display-the-date-and-time-in-the-linux-terminal-and-use-it-in-bash-scripts/
[rkisnah@compute-ops-01002 ~]$ date --utc --date='@1571249945'
Wed Oct 16 18:19:05 UTC 2019
[rkisnah@compute-ops-01002 ~]

# ubuntu printers
http://localhost:631/printers


# ubuntu tabs are slow
https://askubuntu.com/questions/1249405/ubuntu-18-04-20-04-alt-tab-gets-slow-laggy-after-a-while
killall -SIGQUIT gnome-shell


# verify yubikey
yubico-piv-tool -a verify-pin -P 4251421

# generate fingerprint from a private key
ssh-keygen -E md5 -lf ~/.ssh/hpc_test.pub 
3072 MD5:5e:71:f5:e9:47:8e:dd:64:d7:3f:36:66:c3:fe:2a:c4 rkisnah@rkisnah-mac (RSA)

# restart sshd
sudo systemctl restart sshd.service

# emacs on Terminate
set -o emacs

# git log one line 
git log --pretty=oneline

# get public ip via cli
#Ref: https://dev.to/adityathebe/a-handy-way-to-know-your-public-ip-address-with-dns-servers-4nmn
dig +short myip.opendns.com @resolver1.opendns.com -4

# tmux
set -g mouse on 
set -g mouse-select-pane on

# random password generator
# https://www.howtogeek.com/howto/30184/10-ways-to-generate-a-random-password-from-the-command-line/
openssl rand -base64 32
