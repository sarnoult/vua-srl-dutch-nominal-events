#!/usr/bin/python

# This script takes a NAF file that contains a semantic role layer with nominal predicates
# and creates roles for PPs that follow it
# This is a hack for the Dutch NWR processing pipeline to improve event coverage

# Author: Marieke van Erp  marieke.van.erp@vu.nl
# Date: 2 June 2015

import sys
from KafNafParserPy import *
import datetime 

# Read input NAF file
input = sys.stdin
my_parser = KafNafParser(input)

## Create header info
lp = Clp()
lp.set_name('vua-srl-dutch-additional-roles-for-nominal-predicates')
lp.set_version('1.0')
lp.set_timestamp()
my_parser.add_linguistic_processor('srl-extra', lp)

# Create an index of the role ids
role_index = 0
for pred in my_parser.get_predicates():
    for role in pred.get_roles():
        role_number = role.get_id()[1:]
        if int(role_number) > role_index:
                role_index = int(role_number)

# Extract nominal predicates from SRL layer
for pred in my_parser.get_predicates():
    if 'pr-nom' in pred.get_id():
        # Here we get the span target of the predicate
        for span_obj in pred.get_span(): 
           # print pred.get_id(), span_obj.get_id()
            span_index = span_obj.get_id()[2:]
            next_item = int(span_index) + 1
            next_item = 't_' + str(next_item)
           # print span_index, next_item 
            # Get chunks that follow the predicate 
            try:
                for chunk in my_parser.get_constituency_extractor().get_all_chunks_for_term(next_item):
                    # and if they are PPs
                    if chunk[0] == 'pp' and chunk[1][0] == next_item:
            #            print span_index, "t_",next_item, chunk[0], chunk
                        # insert role into NAF
                        role = Crole()
                        role_index = role_index + 1 
                        role.set_id('r' + str(role_index))
                        role.set_sem_role('extra-role')
                        role_span = Cspan()
                        for term_id in chunk[1]:
                            target = Ctarget()
                            target.set_id(term_id)
                            role_span.add_target(target)
                        role.set_span(role_span)
                        pred.add_role(role)
            except KeyError:
                	continue  	

# write new NAF file
my_parser.dump()