# sort_MCNP
Sorts MCNP input file by cell and surface name.

Having a well organized MCNP input file is esspetaily important for large, complex geometries.
Individual cells and surfaces can be renamed using the [numjuggler](https://github.com/inr-kit/numjuggler) tool.
sort_MCNP sorts the newly renamed cells and surfaces by their numerical ID.

sort_MCNP also sorts comments and comment blocks.
It assigns multiple comment lines to the first entity (cell or surface) after them.

Due to it's use of f-strings, the script is compatible with python version 3.6 or later.
It can be modified to be compatible with python 2 by replacing f-strings
with %-formating or the use of `str.format()`.

## How to use ##
Copy the script into the folder with the MCNP input you wish to sort.
Run from terminal as
  
  `python sort_MCNP.py input.i [output_name.i]`,

where the output name is an optional argument.

## Bugs ##
None of the following bugs limit the functionality of the MCNP input. However, they need to be considered to avoid confusion.
 - In it's current form sort_MCNP doesn't correctly assign comments in the middle of multiline cell or surface definitions.
 - It also assigns the first comment block (which ussualy describbes the entire input) to the cell which is defined first.
 - Additionaly, the sctipt assigns the single or multi line comment at the end of the cells block to the surface which is defined first. It also deletes the single or multiline comment at the end of the surfaces block.
These bugs can be seen in the provided example.
