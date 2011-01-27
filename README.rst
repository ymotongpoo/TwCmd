.. -*- coding: utf-8 -*-

TwCmd
=====

This is a sample application that demonstrate how to create command line interface for something using Cmd standard module.


Install
-------

You can user TwCmd easily like this

::
    $ python TwCmd.py


How to use
----------

First of all you have to login with login command.
If you put your authentication info into conf.py beforehand,
you can login without any prompt.

If you are to expand this application and introduce it to a group of users,
just consumer key and secrets are necessary and users have to get PIN code
from the URL shown after login command.

::
    >>> login

Once authenticated properly, you can see your home timeline with tl command.
This command works without any arguments but also accept one arguments that
is the number of tweets printed to the shell. Default number is 30.

::
    >>> tl

    >>> tl 10

You can tweet your message with tw command.
First argument is the content of the message.

::
    >>> tw <your murmur>>


If you want to confirm mentions, you can do it as well with mentions command.

::
    >>> mentions


