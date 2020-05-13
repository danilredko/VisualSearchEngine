import argparse

from model.visual_search import VisualSearch


my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    "-m",
    "--model",
    action="store",
    default="mobile_net_v2",
    type=str,
    help="Specify a model to use",
)

my_parser.add_argument(
    "-img",
    "--image_name",
    action="store",
    type=str,
    default="10000.jpg",
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


model = args.model
image_file = args.image_name
top_k = args.top_k
visual_search = VisualSearch(model)
visual_search.show_top_k(image_file, top_k)
