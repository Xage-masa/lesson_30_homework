import argparse

def main():
    parser = argparse.ArgumentParser(description='Process number and string with options.')
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('text', type=str, help='A string')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--repeat', type=int, default=1, help='Number of times to repeat the string')
    args = parser.parse_args()

    if args.verbose:
        print(f'Received: number={args.number}, text="{args.text}", repeat={args.repeat}')

    print(f'Number: {args.number}, Text: {args.text * args.repeat}')

if __name__ == '__main__':
    main()