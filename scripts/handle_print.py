from pprint import pprint
from datetime import datetime
import click
from prettytable import PrettyTable

# Print pretty with CLI by click


def printTable(data):
    tabla1 = PrettyTable()
    tabla1.align = "l"
    col = ""
    column = {}
    cant = 0

    for key, value in data.items():    
        if isinstance(value, dict):
            for k, v in value.items():
                if isinstance(v, dict):
                    pass
                else:
                    if not isinstance(v, list):
                        col += f'{k} = {v}\n'

            if len(col) > 0:
                column[str(key).upper()] = [col]
                col = ""

        elif isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    pass
                else:
                    col += f'{i}\n'
            if len(col) > 0:
                column[str(key).upper()] = [col]
                col = ""
        else:
            if not isinstance(value, list):
                column[str(key).upper()] = [value]

    del_key_dic = []
    for k, v in column.items():
        tabla1.add_column(k, v)
        cant += 1
        del_key_dic.append(k)
        if cant == 4:
            click.echo(f'\n{tabla1}')
            tabla1.clear()
            cant = 0
    for k in del_key_dic:
        del column[k]
    if len(column) > 0:
        for k, v in column.items():
            tabla1.add_column(k, v)
        click.echo(f'\n{tabla1}')


def printPretty(data):
    for key, value in data.items():
        click.echo('\n====================')
        click.echo(f'{str(key).upper()}\b')
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
                    click.echo(f'* {i}')
        else:
            click.echo(f' * {value}')


def print_history_vt(data):
    table = PrettyTable()
    col = ['Veces Analizado', 'Fecha de Creacion', 'Primera Vista', 'Primera Presentacion',
           'Ultima Presentacion', 'Ultimo Analisis', 'Ultima Modificacion']
    table.field_names = col
    row = []
    click.echo('\n====================')
    click.echo('    HISTORIAL')
    click.echo('====================')
    # click.echo(
    #     '-----------------------------------------------------------')
    try:
        # click.echo(
        #     f'Cantidad de Veces Analizado: {data["times_submitted"]}')
        row.append(data["times_submitted"])
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Creacion: {datetime.fromtimestamp(data["creation_date"])}')
        row.append(data["creation_date"])
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Primera Vista: {datetime.fromtimestamp(data["first_seen_itw_date"])}')
        row.append(data["first_seen_itw_date"])
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Primera Presentacion: {datetime.fromtimestamp(data["first_submission_date"])}')
        row.append(data["first_submission_date"])
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Ultima Presentacion: {datetime.fromtimestamp(data["last_submission_date"])}')
        row.append(datetime.fromtimestamp(data["last_submission_date"]))
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Ultimo Analisis: {datetime.fromtimestamp(data["last_analysis_date"])}')
        row.append(datetime.fromtimestamp(data["last_analysis_date"]))
    except KeyError:
        row.append("---")
    try:
        # click.echo(
        #     f'Fecha de Ultima Modificacion: {datetime.fromtimestamp(data["last_modification_date"])}')
        row.append(datetime.fromtimestamp(data["last_modification_date"]))
    except KeyError:
        row.append("---")
    # # click.echo(
    # #     '-----------------------------------------------------------')
    table.add_row(row)
    click.echo(table)


def print_LAR_vt(data):
    table = PrettyTable()
    col = []
    row = []

    click.echo('\n=============================')
    click.echo('    ANALISIS DE ANITVIRUS')
    click.echo('=============================')
    try:        
        for x in data['last_analysis_results'][0].values():
            for k in x.keys():
                col.append(k)                        
            break
        table.field_names = col

        for i in data['last_analysis_results']:            
            for v in i.values():
                for y in v.values():
                    row.append(y)
                table.add_row(row)
                row.clear()
        click.echo(table)
    except KeyError:
        click.echo("No hay registros")
