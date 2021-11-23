# .bashrc

### User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias rpwd='realpath .'
alias ll='ls -ltrh'
alias re_mount='(
umount /dev/sda2
mount /dev/sda2 /home/sbl/data8TB
)'
alias un_mount='umount /dev/sda2'


PS1='\[\e[0;33m\]\u\[\e[m\]@\h \[\e[4;37m\]\w\[\e[m\] \[\e[1;37m\]%\[\e[m\] '

### Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

### CUDA and cuDNN paths
export PATH=/usr/local/cuda-11.1/bin:${PATH}
export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:${LD_LIBRARY_PATH}
