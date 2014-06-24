# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Development Environment Pre-Requisites
A host machine with the following requirements:

* A Non Virtualized Linux, FreeBSD or Mac OS X environment or Windows 8. Any recent version should work,
    but so far we've tested only on Mac OS X Mavericks and FreeBSD 10.0
* Virtual Box - Latest Version
* Ruby 1.8.7 or superior (not used for production code, but a requirement for vagrant)
* vagrant (please install it from http://www.vagrantup.com/ not from rubygems)
* Python 2.6 or superior (production code is targeted for python 3.3 and runs on it, but ansible requires python 2 on the host machine)
* python-setuptools
* pip

### Initial development setup

Application development must occur inside a virtual machine to ensure a reproducible environment.
This application uses a combination of Vagrant, ansible and shell scripts to make sure this happens.
After installing the pre-requisites pull the code from bitbucket and run from the project root directory

To ensure you have the latest guest additions on the virtual box guest machine, install the vbguest vagrant plugin

$ vagrant plugin install vagrant-vbguest

$ vagrant up
This will setup the virtual machine where you'll run your development code and provision it using ansible
sometimes ssh takes some time to initialize on first boot on the VM, and provisioning fails because of that.
In that case, run
$ vagrant provision

Your source code directory is shared on the virtual machine, so, any changes you do on your host machine, are replicated on the guest machine.
to start/restart the development server run

$ support/localdev.sh server

To run unit tests

$ support/localdev.sh test

To run database migrations

$ support/localdev.sh migrate

If you add any requirements on requirements.txt:

$ support/localdev.sh pip

If you to run any arbitrary django command

$ support/localdev.sh manage.py .....



### some guidelines:

Please note that this is a financial application, so make sure transactions are used
if not familiar with transactions in python, check here
https://docs.djangoproject.com/en/1.6/topics/db/transactions/

By the way, We are using PostgreSQL, no mysql, so you can feel safe knowing that the database supports proper transactions
Also, postgres uses concurrency model called MultiVersioning, instead of simple locking, similar to oracle, so, long transactions are not a impairment to performance like it would be in other dbs like SQL Server or MySQL with InnoDB.

Most of time, @transaction.atomic is your friend, but be aware of the danger of deadlocking.
Also, please remember that is not a good idea to avoid catching exceptions and silencing then inside an atomic block.
Also, make sure to use savepoints where it makes sense, specially when it is interesting for us to have an audit trail
that an operation was attempted.


### Development model.

Use feature branches from master. use pull --rebase to keep your code in sync with the other changes.
When ready to review, use rebase -i to squash your commits into a single commit, push your branch, and open a pull request on bitbucket sending an email to marcos.eliziario@gmail.com to review the code. if everything is ok, I will merge your branch to master, if not, repeat the process.

### About tests:
* Be pragmatic, I don't care if you do strict TDD, but I expect your code to be PROTECTED by your tests. What does it mean? It means that the tests are there to ensure that I and the other developers WON'T BREAK your code without the tests telling us so.
* Public facing features are more important than backend features, So, the level attention of automated tests for those features must be higher
* We are dealing with money, so use the mindset of testing not only that something works, but also test that things that shouldn't happen actually don't happen. Example: It's not enough to test that a customer is able to withdraw money, but also test that he can't withdraw more than her balance on the account.  

### Database migrations

We use south, but as you know, south sometimes create problems when two developers create migrations on differente branches. So, before committing, please give a heads up for the rest of the team that you have a data model change.
