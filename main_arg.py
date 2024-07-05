import sys
import os
import argparse
sys.path.append('/path/to/construc_package')  # Change path
from Class_LassoConstructor import SequenceProcessor

def main():
    parser = argparse.ArgumentParser(description="Construct lasso peptide")

    parser.add_argument('-seq', '--sequence', required=True, help='Sequence to be processed')
    parser.add_argument('-ring_len', type=int, required=True, help='Length of the ring')
    parser.add_argument('-loop_len', type=int, required=True, help='Length of the loop')
    parser.add_argument('-wkdir', '--workdir', required=True, help='Working directory')
    # Add fold_direction argument with default value 'right'
    parser.add_argument('-fold_dir', '--fold_direction', default='right', choices=['left', 'right'], help="Direction of lasso peptide folding: 'right' (default, right-handed) or 'left' (left-handed)")
    
    args = parser.parse_args()

    main_script_dir = os.path.dirname(os.path.abspath(__file__))
    processor = SequenceProcessor(sequence=args.sequence, ring_len=args.ring_len, loop_len=args.loop_len, fold_direction=args.fold_direction, wk_dir=args.workdir, main_script_dir=main_script_dir)
    processor.process_sequence()

if __name__ == "__main__":
    main()
