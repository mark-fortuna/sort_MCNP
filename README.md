# sort_MCNP
Sorts MCNP input file by cell and surface name.

Having a well organized MCNP input file is esspetaily important for large, complex geometries.
Individual cells and surfaces can be renamed using the [numjuggler](https://github.com/inr-kit/numjuggler) tool.
sort_MCNP sorts the newly renamed cells and surfaces by their numerical ID.

sort_MCNP also sorts comments and comment blocks.
It assigns multiple comment lines to the first entity (cell or surface) after them.

For instance:
