from colors_extract import extract_color

def main():
    image = "monet1.jpeg"
    k_values = [3,5,7]
    for k in k_values:
        extract_color(image, k)


if __name__ == '__main__':
    main()
