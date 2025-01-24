from parser import ArtworkParser

def main():
    input_file_path = "files/michelangelo-paintings.html"
    parser = ArtworkParser(input_file_path)
    parser.save_to_json()

if __name__ == "__main__":
    main()
