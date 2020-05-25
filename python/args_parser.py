import argparse


def main(name: str, last_name: str):
    # Simple program to show how to use ArgumentParser
    # Great tutorial on https://realpython.com/command-line-interfaces-python-argparse/
    print(f'name: {name} last name: {last_name}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="First name")
    parser.add_argument("-l", "--lastname", help="Last name")
    args = parser.parse_args()
    main(args.name, args.lastname)
