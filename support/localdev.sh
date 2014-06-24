#!/bin/bash


VAGRANT_MACHINE_NAME=default
LOCAL_SRC_DIR=/var/local/sites/gongaloo/local_src
activate="source ../venv/bin/activate"
pre_cmd="cd $LOCAL_SRC_DIR; . ./activate"

containsElement () {
  local e
  for e in "${@:2}"; do [[ "$e" == "$1" ]] && return 0; done
  return 1
}

which vagrant >/dev/null
if [[ ! $? == 0 ]] ; then
  echo "vagrant executable not found, please install vagrant from www.vagrantup.com"
  exit 1
fi

which VirtualBox >/dev/null
if [[ ! $? == 0 ]] ; then
  echo "VirtualBox executable not found, please install virtualbox from www.virtualbox.org"
  exit 1
fi

which git >/dev/null
if [[ ! $? == 0 ]] ; then
  echo "git not installed, please install it"
  exit 1
fi

if [[ ! "$0" == "support/localdev.sh" ]] ; then
  echo 'Please run this script from the root of your Gongaloo checkout like this: support/localdev.sh'
  echo 'Run "support/localdev.sh help" for more help.'
  exit 1
fi

if [[ "$1" == "help" ]] ; then
  echo "Usage: support/localdev.sh [command]"
  echo
  echo "This script is a helper script for KDVSL Vagrant dev environments"
  echo
  echo "Commands:"
  echo "\thelp    this help screen"
  echo "update    the default mode; updates all necessary dependencies and the vagrant machine"
  echo "test      runs Gongaloo unit tests inside the VM for you"
  echo "server    force restarts the server in a screen on the VM"
  exit 0
fi

if [[ "$1" == "resetdb" ]] || [[ "$1" == "updatedb" ]] ; then
    echo "update db"
fi

if [[ "$1" == "test" ]] ; then
  echo "Running test(s)"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME  -c "sudo su gongaloo -c 'cd $LOCAL_SRC_DIR; pwd; . ./activate ;python manage.py $cmd --failfast'"
  exit $?
fi

if [[ "$1" == "shell" ]] ; then
  echo "Starting shell"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "$pre_cmd ; python manage.py $cmd"
  exit $?
fi

db_cmds=(syncdb migrate)

if [[ ! -z $(echo "${db_cmds[@]:0}" | grep -o $1) ]] ; then
  echo "Running $1"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "sudo su gongaloo -c 'cd $LOCAL_SRC_DIR; pwd; . ./activate ; python manage.py $cmd'"
  exit $?
fi

if [[ "$1" == "pip" ]] ; then
  echo "updating pip"
  shift
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "cd $LOCAL_SRC_DIR; sudo su gongaloo -c '. ./activate; pip install -r requirements.txt'"
  exit $?
fi

if [[ "$1" == "schemamigration" ]] ; then
  echo "running $@"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "cd $LOCAL_SRC_DIR; pwd; . ./activate ; python manage.py $cmd"
  exit $?
fi

if [[ "$1" == "manage.py" ]] ; then
  shift
  echo "running $@"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "sudo su gongaloo -c 'cd $LOCAL_SRC_DIR; pwd; . ./activate ; python manage.py $cmd'"
  exit $?
fi

if [[ "$1" == "behave" ]] ; then
  shift
  echo "running behave $@"
  cmd=$@
  vagrant ssh $VAGRANT_MACHINE_NAME -c "sudo killall Xvfb; export DISPLAY=:99"

  vagrant ssh $VAGRANT_MACHINE_NAME -c "sudo su gongaloo -c 'export DISPLAY=:99; Xvfb :99 -ac -screen 0 1280x1024x24 > /dev/null 2>&1 & cd $LOCAL_SRC_DIR; pwd; . ./activate ; behave $cmd'"
  exit $?
fi



if [[ "$1" == "server" ]] ; then
  echo "Force killing any running python and tmux processes; then starting the server"
  vagrant ssh -c 'killall -9 python 1>/dev/null 2>&1 ; \
    killall -9 tmux 1>/dev/null 2>&1 ; \
    tmux new-session -d -s Gongaloo ; tmux send-keys "sudo su gongaloo " "C-m"; \
    tmux send-keys "cd /var/local/sites/gongaloo/local_src; . ./activate" "C-m" ; \
    tmux send-keys "python manage.py runserver 0.0.0.0:8000" "C-m" ; \
    sleep 5 ; test $(ps aux | grep runserver | grep -v grep | wc -l) -eq 2'
  RETURN=$?
  if [[ $RETURN -eq 0 ]] ; then
    echo "Server is running!"
  else
    echo "Server failed to start; login with 'vagrant ssh' then type 'tmux attach-session -t Gongaloo' to see the output"
  fi
  exit $RETURN
fi

# No command, or update, means update, so here we go
if [[ "$1" == "update" || "$1" == "" ]] ; then
  echo "Updating / Launching Vagrant Machine as needed!"
  echo "====== Updating vagrant machine"
  VAGRANT_MACHINE_STATUS="$(vagrant status | grep $VAGRANT_MACHINE_NAME | awk '{print $2}')"
  if [[ "$VAGRANT_MACHINE_STATUS" == "running" ]] ; then
    vagrant provision $VAGRANT_MACHINE_NAME
  else
    vagrant up $VAGRANT_MACHINE_NAME
  fi

  exit 0
fi

# Okay everything is all done; if we got here we didn't hit a previous exit code and the user gave bad input
echo "Something went wrong if you're seeing this."
echo "For more information, run: support/localdev.sh help"
exit 1
