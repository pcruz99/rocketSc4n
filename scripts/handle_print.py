from pprint import pprint
from datetime import datetime
import click

# Print pretty with CLI by click
def printPretty(data):
    for key, value in data.items():
        click.echo('\n====================')
        click.echo(f'{str(key).upper()}')
        click.echo('====================')

        if isinstance(value, dict):
            for k, v in value.items():
                if isinstance(v, dict):
                    pprint(value)
                else:
                    click.echo(f'{k}    =   {v}')
        elif isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    pprint(i)
                else:
                    click.echo(f'- {i}')
        else:
            click.echo(f'- {value}')


def printHistory(data):
    click.echo('\n====================')
    click.echo('    HISTORIAL')
    click.echo('====================')
    click.echo(
        '-----------------------------------------------------------')
    try:
        click.echo(
            f'Cantidad de Veces Analizado: {data["times_submitted"]}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Creacion: {datetime.fromtimestamp(data["creation_date"])}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Primera Vista: {datetime.fromtimestamp(data["first_seen_itw_date"])}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Primera Presentacion: {datetime.fromtimestamp(data["first_submission_date"])}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Ultima Presentacion: {datetime.fromtimestamp(data["last_submission_date"])}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Ultimo Analisis: {datetime.fromtimestamp(data["last_analysis_date"])}')
    except KeyError:
        pass
    try:
        click.echo(
            f'Fecha de Ultima Modificacion: {datetime.fromtimestamp(data["last_modification_date"])}')
    except KeyError:
        pass
    click.echo(
        '-----------------------------------------------------------')


def printLAR(data):
    click.echo('\n  ANALISIS DE ANITVIRUS\n')    
    try:
        for i in data['last_analysis_results']:
            for k, v in i.items():
                click.echo('====================')
                click.echo(str(k).upper())
                click.echo('====================')
                for x, y in v.items():
                    click.echo(f'{x}: {y}')
                click.echo("\n")
    except KeyError:
        click.echo("No hay registros")
