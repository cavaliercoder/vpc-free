vpc-free
========

This script searches for the largest available IP subnets within the unallocated
spaces between your VPC subnets, or between VPCs for a given CIDR block.

Installation
------------

Install ``vpc-free`` to ``/usr/local/bin`` with:

.. code-block:: shell

    $ pip install vpc-free

The script uses the Amazon AWS SDK (``boto3``) to connect to AWS. The SDK must
be configured with credentials to connect to the AWS APIs. Please see the `Boto3
documentation`_ for instruction.

.. _Boto3 Documentation: http://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration

Usage
-----

.. code-block:: shell

    $ vpc-free -h
    usage: vpc-free [-h] [TARGET]

    Find free IP blocks in AWS EC2.

    positional arguments:
      TARGET      CIDR, VPC ID or VPC Name to search

    optional arguments:
      -h, --help  show this help message and exit

Example
-------

.. code-block:: shell

    # search between subnets in this default VPC - 172.31.0.0/16
    $ vpc-free 
    MIN IP      MAX IP         MASK SIZE  BEST            LABEL
    172.31.0.0  172.31.15.255  /20  4096                  subnet-b93bafd0
    172.31.16.0 172.31.31.255  /20  4096                  subnet-a63acfcf
    172.31.32.0 172.31.47.255  /20  4096                  subnet-7daffd3b
    172.31.48.0 172.31.255.255      53248 172.31.128.0/17 FREE  
