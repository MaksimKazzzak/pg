import sys

def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, 'rb') as file:
        return file.read(header_length)


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    jpeg_header = b'\xff\xd8'
    return read_header(file_name, len(jpeg_header)) == jpeg_header


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # vyhodnoť zda je soubor gif
    gif_header1 = b'GIF87a'
    gif_header2 = b'GIF89a'
    return read_header(file_name, len(gif_header1)) in [gif_header1, gif_header2]


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # vyhodnoť zda je soubor png
    png_header = b'\x89PNG\r\n\x1a\n'
    return read_header(file_name, len(png_header)) == png_header


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(f"Soubor nenalezen")
    except FileNotFoundError:
        print(f"Název souboru není správně zadán")
    except Exception as e:
        print(f"Došlo k chybě {e}.")
    else:
        print_file_type(file_name)

if __name__ == '__main__':
    main()
