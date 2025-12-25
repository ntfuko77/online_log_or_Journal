import argparse



def args_not_empty(args):
    for arg in vars(args):
        if getattr(args, arg) is not None:
            return True
    return False
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