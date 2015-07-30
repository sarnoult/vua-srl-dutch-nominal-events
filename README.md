VUA SRL Dutch additional roles
==============

Description
------------
This is an SRL postfix hack that adds semantic roles for nominal events that were added to the predicate layer after the regular SRL module was run. It only creates roles for PPs that follow the nominal event.

Prerequisites
-----------
[KafNafParserPy](https://github.com/cltl/KafNafParserPy "KafNafParserPy")

Usage
--------
cat input.naf | python vua-srl-dutch-additional-roles.py

Contact
-------
Marieke van Erp
marieke.van.erp@vu.nl
VU University Amsterdam

License
----------
Apache v2. See LICENSE file for details. 