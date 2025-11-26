import argparse
import sys



def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--config', type=str, default='config.yaml', help='Path to the configuration file')
    return parser
def parse_args():
    parser=create_parser()
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(sys.argv)
    print(args)
else:
    ...