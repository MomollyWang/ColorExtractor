# import extractor.colors_extract
import sys
from extractor import colors_extract

def main():
    image = sys.argv[1]
    k_values = 5
    colors_extract.extract_color(image, k_values)


if __name__ == '__main__':
    main()
