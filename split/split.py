import click

from pathlib import Path

@click.command()
@click.argument('filepath')
@click.option('-h', '--header', is_flag=True)
@click.option('-c', '--chunk-size', default=50, type=int)
def main(filepath, header, chunk_size):
    filepath = Path(filepath)
    filename = filepath.stem
    dir_path = filepath.parent

    def chunks(list_):
        for i in range(0, len(list_), chunk_size):
            yield list_[i:i + chunk_size]

    with open(filepath, 'r') as f:
        lines = f.readlines()
        if header:
            colnames, lines = lines[0], lines[1:]
        for i, chunk in enumerate(chunks(lines)):
            new_path = dir_path / f'{filename}_{i}.csv'
            with open(new_path, 'w') as f:
                f.write('\n'.join(chunk))

if __name__ == "__main__":
    main()