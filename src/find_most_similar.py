import argparse

from model.similarity_finder import SimilarityFinder


def main():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument(
        "-img",
        "--image_name",
        action="store",
        type=str,
        default="13573.jpg",
        help="Specify a name of image to find similar images for",
    )

    my_parser.add_argument(
        "-k",
        "--top_k",
        action="store",
        type=int,
        default=4,
        help="how many similar images to show",
    )
    args = my_parser.parse_args()

    image_file = args.image_name
    top_k = args.top_k

    similarity_finder = SimilarityFinder()
    similarity_finder.show_top_k(image_file, top_k)


if __name__ == "__main__":
    main()
