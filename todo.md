## mkessler-bibliography
    - Add option for only images / literature
    - Add option to set include paths of images / literature

## mkessler-hypersetup
    - Get rid of \@course - replace with \@title by default (automatically detect this?)

## castel-figures
    - Add option for include path of inkscape figures



### Option clashes
There is an option clash (since TexLive 2018) between thmtools, IEEEtrantools and cleveref.
 To (temporarily) fix this, the hypersetup package provides cleveref only as an option 'cleveref'. Only load this if you are not using both of the abve

See also
https://tex.stackexchange.com/questions/515560/incompatibility-of-thmtools-ieeetrantools-and-cleveref-in-tex-live-2018-2019



## Ideas for new macros

- Cup with point above for disjoint union
- Print a complex number i differently
- function restriction (f|_X f\mid_X is not nice, take spacing from \upharpoonright ?) l. 156 \defon
- macro for 'entspricht'
- cev for reversed direction vector, l. 170 \cev
- integration for mathbf?

# Package reworks
## mkessler-mathfonts
- get old calligraphic font and provide it as \mathcalo
- 
## mkessler-fancythm
- spacing of subsection before fancy thm


# Package ideas 
- Define new math environment column types

