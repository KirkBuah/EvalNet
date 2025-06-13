# Delorme Analysis

## Compile

```bash
make
```


## Run

```bash
./analyze -q <q> -i <input_adj_mat> -o <output_neigh_cluster_offset_tuple>
```


## Example

```bash
./analyze -q 8 -i ../../data/Delormes/Delorme.8.adj.txt -o dump
```

The output "dump" contains the adjacency lists with ``(neighbor, neighbor_cluster, neighbor_offset)`` tuples.
