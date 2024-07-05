# LassoHTP2.0

LassoHTP2.0 constructs 3D structures of lasso peptides using input parameters such as lasso peptide **sequence**, **ring length**, and **loop length**. It generates optimized structures through MD minimization and provides force field and MD input files for the constructed structures. Users can run MD simulations as needed to obtain a relaxed lasso peptide structure.

<p align="center">
  <img width="650" height="300" src="https://github.com/so-dopamine/LassoHTP/blob/main/image.jpg">
</p>

LassoHTP2.0 is available for loop lengths from 3 to 50 and constructs lasso peptide structures for sequences within 30 amino acids in approximately 1-3 minutes.

## Requirements

Ensure your Linux environment (python=3.10) includes the following software:
- **Amber:** `pmemd.MPI` (and `pmemd.cuda` if you want a relaxed structure with MD production)
- **PyMOL:** `pymol -c`

Hardware and parallel computing:

- **CPU:** A 16-core CPU is recommended (and a GPU if you want a relaxed structure with MD production).
- **MPI:** Install MPI and use the `mpirun` command to enable parallel computing capabilities.

## Install

We recommend using a conda environment.

1. Build and activate a new environment:

```bash
conda create -n lassohtp python=3.10
source activate lassohtp
```

2. Install PyMOL:

```bash
conda install conda-forge::pymol-open-source
```

4. Install Amber 

See [Amber Installation Guide](https://ambermd.org/Installation.php)


## Usage

```bash
python main_arg.py  -seq <sequence> -ring_len <ring_length> -loop_len <loop_length> -wkdir <workdir> [-fold_dir {left,right}]
```

### Arguments
`-seq`, `--sequence`: The sequence for prediction (required).

`-ring_len`: The ring length of the input lasso peptide. Ensure the corresponding amino acid is located on either Asp or Glu.

`-loop_len`: The loop length of the input lasso peptide. Ensure it is within the range of 3 to 50, and that the tail length (total sequence length minus ring length and loop length) is at least 2.

`-wkdir`, `--workdir`: The work directory name defined by the user (required).

`-fold_dir`, `--fold_direction`: The direction of folding for the lasso peptide ring (optional). Choices are left or right (default: right).

*A left-handed lasso peptide involves the N-terminus wrapping around the tail in a counterclockwise direction, while a right-handed lasso peptide would involve the N-terminus wrapping in a clockwise direction. See [reference](https://doi.org/10.1021/acs.jpcb.3c08492)*.

## Example

```bash
python main_arg.py -seq LGSSGKYTDAAFGSHTPIDDITFES -ring_len 9 -loop_len 6 -wkdir test1
python main_arg.py -seq GLWWGCPQDVFGGLTPLAC -ring_len 9 -loop_len 3 -wkdir test2
python main_arg.py -seq LLNSSGNDRLVLSKN -ring_len 8 -loop_len 5 -wkdir test3
python main_arg.py -seq GMGGLREDLAIGEPFTGLADD -ring_len 7 -loop_len 8 -wkdir test4
```

## Output

The directory under the work directory you specified will include:

- Optimized structures: `final_output/min1_clean.pdb`
- MD simulation folder: `raw_output/MDprod/`, which includes structural and parameter files for the lasso peptide system and related MD input files.

## Note

There may be situations where the structure cannot be successfully constructed for various reasons. To ensure a successful attempt, please adhere to the following guidelines:

- **Valid Characters**: The sequence should only contain standard amino acids: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y. Sequences with any non-standard characters will be automatically rejected.
- **Isopeptide Residues**: Ensure that the specified ring length is compatible with amino acids capable of forming isopeptide bonds. Please note that only Asp(D) and Glu(E) can form these bonds.
- **Sequence Length**:  LassoHTP2.0 cannot construct structures if the loop length exceeds 50 due to a limited scaffold library, as the lasso peptide lengths above 60 are uncommon. If the tail length (total sequence length minus the ring and loop lengths) is less than 2 amino acids, an error will occur. The sequence must be at least 12 amino acids long to accommodate the minimum requirements: a ring length of 7, a loop length of 3, and a tail length of 2.

