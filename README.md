# sort_MCNP
Sorts MCNP input file by cell and surface name.

Having a well organized MCNP input file is esspetaily important for large, complex geometries.
Individual cells and surfaces can be renamed using the [numjuggler](https://github.com/inr-kit/numjuggler) tool.
sort_MCNP sorts the newly renamed cells and surfaces by their numerical ID.

sort_MCNP also sorts comments and comment blocks.
It assigns multiple comment lines to the first entity (cell or surface) after them.

## Bugs ##
None of the following bugs limit the functionality of the MCNP input. However, they need to be considered to avoid confusion.
 - In it's current form sort_MCNP doesn't correctly assign comments in the middle of multiline cell or surface definitions.
 - It also assigns the first comment block (which ussualy describbes the entire input) to the cell which is defined first.
 - Additionaly, the sctipt assigns the single or multi line comment at the end of the cells block to the surface which is defined first. It also deletes the single or multiline comment at the end of the surfaces block.
These bugs can be seen in the example below.

## Example ##
  example for sort_MCNP
  c example from:
  c   MCNP — A General Monte Carlo N-Particle Transport Code, Version 5,
  c   Volume II: User’s Guide,
  c   chapter 4, example 2
  c Cells have been shuffled and comments added to demonstrate sort_MCNP script
  c
  c CELLS
  5 like 2 but trcl=5 imp:n=1
  c comment before cell 1
  1 1 -.5 -7 #2 #3 #4 #5 #6 imp:n=1
  9 like 8 but trcl=(.9 .9 0)
  4 like 2 but trcl=4
  c
  3 like 2 but trcl=3  $ blank comment before cell 3
  6 like 2 but trcl=6
  c multi line comment before cell 2
  c
  c third line of comment before cell 2
  2 0 1 -2 -3 4 5 -6 imp:n=2 trcl=2 fill=1
  7 0 7 imp:n=0
  c single line coment before cell 12
  12 2 -18 -12 imp:n=1 trcl=(-.3 .3 0) u=2
  11 2 -18 #8 #9 #10 imp:n=1 u=1
  8 0 8 -9 -10 11 imp:n=1 trcl=(-.9 .9 0) fill=2 u=1
  14 like 12 but trcl=(.3 -.3 0)
  15 like 12 but trcl=(-.3 -.3 0)
  10 like 8 but trcl=(.1 -.9 0)
  16 1 -.5  $ cell 16 has multi line definition
       #12 #13 #14
  c comment in the midle of cell 16 definition
       #15 u=2 imp:n=1
  13 like 12 but trcl=(.3 .3 0)
  c comment at the end of CELLS block

  c SURFACES
  c
  3 px 2
  8 px -.7
  c multiline comment before surface 10
  c
  c
  c
  10 px .7
  5 pz -2
  2 py 2
  12 cz .1
  6 pz 2
  c comment before surface 1
  1 px -2
  9 py .7
  4 py -2
  7 so 15
  11 py -.7
  c comment at the end of SURFACES block
