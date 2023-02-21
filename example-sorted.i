example for sort_MCNP
c comment before cell 1
1 1 -.5 -7 #2 #3 #4 #5 #6 imp:n=1
c multi line comment before cell 2
c
c third line of comment before cell 2
2 0 1 -2 -3 4 5 -6 imp:n=2 trcl=2 fill=1
c
3 like 2 but trcl=3  $ blank comment before cell 3
4 like 2 but trcl=4
c example from:
c   MCNP — A General Monte Carlo N-Particle Transport Code, Version 5,
c   Volume II: User’s Guide,
c   chapter 4, example 2
c Cells have been shuffled and comments added to demonstrate sort_MCNP script
c
c CELLS
5 like 2 but trcl=5 imp:n=1
6 like 2 but trcl=6
7 0 7 imp:n=0
8 0 8 -9 -10 11 imp:n=1 trcl=(-.9 .9 0) fill=2 u=1
9 like 8 but trcl=(.9 .9 0)
10 like 8 but trcl=(.1 -.9 0)
11 2 -18 #8 #9 #10 imp:n=1 u=1
c single line coment before cell 12
12 2 -18 -12 imp:n=1 trcl=(-.3 .3 0) u=2
c comment in the midle of cell 16 definition
13 like 12 but trcl=(.3 .3 0)
14 like 12 but trcl=(.3 -.3 0)
15 like 12 but trcl=(-.3 -.3 0)
16 1 -.5  $ cell 16 has multi line definition
     #12 #13 #14
     #15 u=2 imp:n=1

c comment before surface 1
1 px -2
2 py 2
c comment at the end of CELLS block
c SURFACES
c
3 px 2
4 py -2
5 pz -2
6 pz 2
7 so 15
8 px -.7
9 py .7
c multiline comment before surface 10
c
c
c
10 px .7
11 py -.7
12 cz .1

c DATA
sdef erg=d1 cel=d2:d3:0 rad=d5 ext=d6 axs=0 0 1 pos=d7
#    si1  sp1   sb1
      1    0     0
      3   .22   .05
      4   .08   .05
      5   .25   .1
      6   .18   .1
      7   .07   .2
      8   .1    .2
      9   .05   .1
      11  .05   .2
si2 L 2 3 4 5 6
sp2 1 1 1 1 1
si3 L 8 9 10
sp3 1 1 1
si5 0 .1
sp5 -21 1
si6 -2 2
sp6 0 1
si7 L .3 .3 0 .3 -.3 0 -.3 .3 0 -.3 -.3 0
sp7 1 1 1 1
m1 6000 1
m2 92235 1
drxs
tr2 -6 7 1.2
tr3 7 6 1.1
tr4 8 -5 1.4
tr5* -1 -4 1 40 130 90 50 40 90 90 90 0
tr6 -9 -2 1.3
f4:n 2 3 4 5 6 12 13 14 15
e4 1 3 5 7 9 11 13
sd4 5j 1.8849555921 3r
fq f e
cut:n 1e20 .1
nps 100000