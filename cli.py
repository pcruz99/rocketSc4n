import click
from datetime import datetime
from pprint import pprint
from core import __version__
from core import explore_file, explore_url, delete_all_urls, delete_all_files
from scripts import printPretty, printHistory, printLAR


@click.version_option(
    __version__, "-V", "--version", message="rocketSc4n, version %(version)s"
    # message="%(prog)s, version %(version)s"
)
@click.group()
def cli(max_content_width=120):   
    """
    ----------------------------------------------------------------------------
    -------------|--------------------------------#####-------------------------
    ------------/|\------------------------------#-----#-------------#----------
    ------------/-\------------------------------#-----#-----------###----------
    --#####----/###\---####--#----#-######-#####-#--------####----#--#--#----#--
    --#----#--|#---#|-#----#-#---#--#--------#----#####--#----#--#---#--##---#--
    --#----#--|#---#|-#------####---#####----#---------#-#------#----#--#-#--#--
    --#####---|#---#|-#------#--#---#--------#---#-----#-#------#######-#--#-#--
    --#---#---|\###/|-#----#-#---#--#--------#---#-----#-#----#------#--#---##--
    --#----#-/|=====|\-####--#----#-######---#----#####---####-------#--#----#--
    ---------/-\_^_/-\----------------------------------------------------------
    --======----^^^----=======================================================--
    --======---^^^^^---=======================================================--
    ----------------------------------------------------------------------------

    sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """             
    pass

# *************************************************************************************************************


@cli.command(help="Explore File: Comand to get report about a file known")
@click.option('-p', '--path', required=True, type=str, help="Path for the file")
@click.option('-h', '--hash-alg',
              required=False,
              help="Hashing Algorithm for the file",
              type=click.Choice(['md5', 'sha1', 'sha256']),
              default='md5',
              show_default=True
              )
@click.option('-e', '--engine',
              required=False,
              help="Engine for de scan or search",
              type=click.Choice(['vt', 'kp']),
              default='vt',
              show_default=True
              )
@click.option('-a', '--anls-antv', is_flag=True, help="Aanalisis de los Anitvirus")
@click.option('-H', '--history', is_flag=True, help="Aanalisis de los Anitvirus")
@click.option('-v', '--verbose', is_flag=True, help="Resumir lo mas Importante")
@click.option('-U', '--update', is_flag=True, help="Actualizar el Ultimo Escaneo, no utilzarlo si no ha escaneado previamente")
@click.option('-c', '--chat-gpt', is_flag=True, help="Utilizar ChatGPT para explicar los resultados")
@click.pass_context
def expl_file(ctx, path, hash_alg, engine, anls_antv, history, verbose, update, chat_gpt):
    if not path:
        ctx.fail("The file path is required")
    else:
        data = explore_file(path, hash_alg, engine, update=update)

        if engine == 'vt' and anls_antv:
            printLAR(data)
        elif engine == 'vt' and history:
            printHistory(data)
        else:
            printPretty(data)

# *************************************************************************************************************

@cli.command(help="Explore Url: Comand to get report about a url of website known")
@click.option('-u', '--url', required=True, type=str, help="URL for the web")
@click.option('-e', '--engine',
              required=False,
              help="Engine for de scan or search",
              type=click.Choice(['vt', 'kp']),
              default='vt',
              show_default=True              
              )
@click.option('-a', '--anls-antv', is_flag=True, help="Aanalisis de los Anitvirus")
@click.option('-H', '--history', is_flag=True, help="Aanalisis de los Anitvirus")
@click.option('--verbose', is_flag=True, help="Resumir lo mas Importante")
@click.option('-U', '--update', is_flag=True, help="Actualizar el Ultimo Escaneo, no utilzarlo si no ha escaneado previamente")
def expl_url(url, engine, anls_antv, history, verbose, update):
    
    data, status = explore_url(url=url, engine=engine, update=update)
    print(f'\n{status}')

    if engine == 'vt' and anls_antv:
        printLAR(data)
    elif engine == 'vt' and history:
        printHistory(data)
    else:
        printPretty(data)

# *************************************************************************************************************

@cli.command(help="Eliminar la base de datos local de los files.")
@click.option('--confirm', prompt='Desea eliminar TODOS los files registrados', type=click.Choice(['y','n']))
def delreg_files(confirm):
    if confirm == 'y':
        status = delete_all_files()
        print(f'\n{status}\n')
    else:
        print('\nABORTADO\n')

@cli.command(help="Eliminar la base de datos local de las urls.")
@click.option('--confirm', prompt='Desea eliminar TODAS las urls registradas', type=click.Choice(['y','n']))
def delreg_urls(confirm):
    if confirm == 'y':
        status = delete_all_urls()
        print(f'\n{status}\n')
    else:
        print('\nABORTADO\n')

# @cli.command()
# def scan_file():
#     pass


# @cli.command()
# def scan_url():
#     pass
