# Topology Generation

## Hypercube
```
usage: tool.py generate hypercube [-h] [-v] n

positional arguments:
  n               specifies number of dimensions

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Torus
```
usage: tool.py generate torus [-h] [-v] n k

positional arguments:
  n               specifies number of dimensions
  k               specifies number nodes per "edge"

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Flattened Butterfly
```
usage: tool.py generate flatbutterfly [-h] [-v] n k

positional arguments:
  n               specifies number of dimensions
  k               specifies k

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Multi-Layer Full-Mesh
```
usage: tool.py generate mlfm [-h] [-v] h

positional arguments:
  h               specifies degree of local routers

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Two-Level Orthogonal Fat-Tree
```
usage: tool.py generate oft [-h] [-v] k

positional arguments:
  k               specifies degree of routers in Layer 0 and Layer 2 (k:= q + 1 where q is prime)

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Jellyfish
```
usage: tool.py generate jellyfish [-h] [-v] r n

positional arguments:
  r               specifies network radix/degree of routers/nodes
  n               total number of routers/nodes

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## HyperX
```
usage: tool.py generate hyperx [-h] [-v] l s

positional arguments:
  l               specifies number of dimensions
  s               number of nodes per dimension

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## DragonFly
```
usage: tool.py generate dragonfly [-h] [-v] p

positional arguments:
  p               number of hosts per router

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## FatTree
```
usage: tool.py generate fattree [-h] [-v] k

positional arguments:
  k               network radix of routers (must be even)

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Xpander
```
usage: tool.py generate xpander [-h] [-v] d lifts [lifts ...]

positional arguments:
  d               specifies the initial d-regular complete graph
  lifts           specifes the random lifts

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Slim Fly
```
usage: tool.py generate slimfly [-h] [-v] q

positional arguments:
  q               specifies the size of Galois field (q:=4w + delta where delta = -1 or 0 or 1 and q a prime power)

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Delorme
```
usage: tool.py generate delorme [-h] [-v] q

positional arguments:
  q               specifies the size of Galois field (q: size of Galois field, q:= 2^(2*a-1), where a = 1,2,3,... and q an odd power of 2)

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Brown
```
usage: tool.py generate brown [-h] [-v] q

positional arguments:
  q               specifies the size of Galois field (q: size of Galois field, is a prime power

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Incremental Expansions of a Brown Topology
```
usage: tool.py generate brown_ext [-h] [-v] q r0 r1

positional arguments:
  q               specifies the size of Galois field (q: size of Galois field, is a prime power)
  r0              number of replications of cluster C0
  r1              round robin replication of a selected quadric and its neighbors(if r1>0, r0 is ignored)

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## BundleFly
```
usage: tool.py generate bundlefly [-h] [-v] q

positional arguments:
  q               degree

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Kautz
```
usage: tool.py generate kautz [-h] [-v] b n

positional arguments:
  b               base
  n               length

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Arrangement Network
```
usage: tool.py generate arrnetwork [-h] [-v] n k

positional arguments:
  n               maximum integer
  k               permutations

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Extended Generalized FatTree
```
usage: tool.py generate xgft [-h] [-v] h inputs [inputs ...]

positional arguments:
  h               height
  inputs          specifes number of childs and parents per level. [c1,c2,...,ch,p1,p2,...,ph]

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## k-ary-n Tree
```
usage: tool.py generate karyn [-h] [-v] k n

positional arguments:
  k               half the number of ports per switch
  n               numbers of levels in the tree

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Mesh
```
usage: tool.py generate mesh [-h] [-v] n k g

positional arguments:
  n               Number of dimensions
  k               Number of routers per edge
  g               gap

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Tofu
```
usage: tool.py generate tofu [-h] [-v] n [n ...]

positional arguments:
  n               Array of dimension of mesh n1xn2x..xnN

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## Cascade Dragonfly
```
usage: tool.py generate casdf [-h] [-v] g

positional arguments:
  g               number of groups

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## SpectralFly
```
usage: tool.py generate specfly [-h] [-v] p q

positional arguments:
  p               parameter p, must be odd prime
  q               parameter q, must be odd prime distinct from p

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## MegaFly
```
usage: tool.py generate megafly [-h] [-v] g d

positional arguments:
  g               total number of groups
  d               total radix, must be even

optional arguments:
  -h, --help      show this help message and exit
  -v, --validate  validates the generated topology
```

## PolarStar
```
usage: tool.py generate polarstar [-h] [-v] d pfq jq [{bdf,paley,max}]

positional arguments:
  d                degree
  pfq              Parameter for polarfly stucture graph
  jq               Parameter for subgraph (bdf or paley)
  {bdf,paley,max}  subgraph

optional arguments:
  -h, --help       show this help message and exit
  -v, --validate   validates the generated topology
```
