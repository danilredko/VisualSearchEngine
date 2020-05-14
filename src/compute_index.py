import os
import argparse

from model.feature_computation import FeatureComputer


def main():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument(
        "-m",
        "--model",
        action="store",
        default="mobile_net_v2",
        type=str,
        help="Specify a model to use",
    )
    args = my_parser.parse_args()
    model = args.model

    if not os.path.exists("data"):
        os.makedirs("data")

    index_builder = FeatureComputer(model)
    index_builder.save_filenames()


if __name__ == "__main__":
    main()
