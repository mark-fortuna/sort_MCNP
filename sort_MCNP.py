# script to sort all cells and surfaces by name
#
# comments and comment blocks are bound to next entity (cell or surface)

import regex as re
import sys


###   READ TERMINAL ARGUMENTS   ###

if len(sys.argv) == 1:
    print('\nTo run sort_MCNP.py specify file to be sorted. Eg.:\n  python sort_MCNP.py inpt.i [new_name.i]\nHere, the argument in square brackets is optional.\n')
    quit()
elif len(sys.argv) == 2:
    file_name = sys.argv[1]
    suffix = '.' + file_name.split('.')[-1]
    no_suffix = re.sub(suffix, '', file_name)
    out_name = no_suffix + '-sorted' + suffix
else: 
    file_name = sys.argv[1]
    out_name = sys.argv[2]

delete_comments = False


###   CLASSES   ###

# a Card object is either a Cell definition or a Surface definition
class Card:
    def __init__(self, name, definition, entity_type):
        self.type = entity_type
        self.name = name
        self.definition = definition
        self.prepended_comment = None

    def __str__(self):
        if delete_comments:
            return f'{self.name}{self.definition}'
        elif self.prepended_comment:
            return f'{self.prepended_comment}{self.name}{self.definition}'
        else:
            return f'{self.name}{self.definition}'

    def __repr__(self):
        if self.prepended_comment:
            return f'Card(name = {self.name}, definition = {self.definition}, type = {self.type}, prepended comment = {self.prepended_comment})'
        else:
            return f'Card(name = {self.name}, definition = {self.definition}, type = {self.type})'

    def AppendDefinition(self, more_definition):
        self.definition += more_definition

    def PrependComment(self, comment_lines):
        joined_lines = ''
        for i in comment_lines:
            joined_lines += i + '\n'
        self.prepended_comment = joined_lines

    def CardInfo(self):
        return f'{self.type} {self.name} is defined as:\n{self.name}{self.definition}'

    def Write(self):
        return f'{self.name}{self.definition}'

    def GetType(self):
        return f'{self.type}'


###   FUNCTIONS   ###

# The following functions are performed on individual MCNP input lines

def previous_card(line):
    # checks if 'line' describes previous card
    #   'line' is multiline description --> return TRUE
    #   'line' is new entity --> return FALSE 
    return bool(re.search(r'^(\s{5})', line))

def comment(line):
    # is 'line' a comment?
    return bool(re.search(r'^c', line, re.IGNORECASE))

def seperate_name_and_definition(line):
    match_name = re.search(r'(\s*)(\d+)', line)
    space_and_name = match_name.group(0)
    name = re.sub(r'\s*', '', space_and_name)
    end_of_name = match_name.end()
    definition = line[end_of_name:]
    return name, definition


###   MAIN   ###

file = open(file_name, 'r')
everything = file.read()
cells, surfaces, other = everything.split('\n\n')

title_line = cells.split('\n')[0]
cell_lines = cells.split('\n')[1:]  # skip first line - title
surf_lines = surfaces.split('\n')
other_lines = other.split('\n')

stored_comment = []

##  MAKE CELL OBJECTS  ##
cell_cards = []
for i,l in enumerate(cell_lines):
    # if first line starts with
    #   4 or less spaces AND
    #   doesn't start with a letter
    # it's a cell or surface definition
    # else: it's a comment or a definition for previous entity
    if previous_card(l): # append line to definition of previous card
        # print(f'From previous card: {l}')
        cell_cards[-1].AppendDefinition(f'\n{l}')
    elif comment(l):
        stored_comment.append(l)
    else: # card is definition of new entity
        name, definition = seperate_name_and_definition(l)
        cell_cards.append(Card(name, definition, entity_type='cell'))
        cell_cards[-1].PrependComment(stored_comment)
        stored_comment = []

##  MAKE SURFACE OBJECTS  ##
surf_cards = []
for i,l in enumerate(surf_lines):
    if previous_card(l):
        # print(f'From previous card: {l}')
        surf_cards[-1].AppendDefinition(f'\n{l}')
    elif comment(l):
        stored_comment.append(l)
    else:
        name, definition = seperate_name_and_definition(l)
        surf_cards.append(Card(name, definition, entity_type='surface'))
        surf_cards[-1].PrependComment(stored_comment)
        stored_comment = []

print(f'number of cells = {len(cell_cards)}')
print(f'number of surfaces = {len(surf_cards)}')

##  SORT CELLS AND SURFACES  ##
sorted_cell_cards = sorted(cell_cards, key=lambda x: int(x.name), reverse=False)
sorted_surf_cards = sorted(surf_cards, key=lambda x: int(x.name), reverse=False)

##  WRITE TO OUTPUT FILE  ##
out = open(out_name, 'w')
out.write(f'{title_line}\n')
for i in sorted_cell_cards:
    out.write(f'{str(i)}\n')
out.write('\n')
for i in sorted_surf_cards:
    out.write(f'{str(i)}\n')
out.write(f'\n{other}')
