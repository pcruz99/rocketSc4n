"""
    Tuplas definidas con variables que son utilizadas para extraer informacion
    del JSON respuesta de la solicitud a la API de VirusTotal
"""
# Estas tuplas se utilizan para la funcion "get_file_report"
# This tuples is used to the functions "get_file_report"

atrs_file = (    
    #history---init
    'creation_date',
    'first_seen_itw_date',
    'first_submission_date',
    'last_submission_date',
    'last_analysis_date',
    'last_modification_date',
    'times_submitted',
    #history---end
    #detection--init
    'total_votes',
    'last_analysis_stats',
    'popular_threat_classification',
    'sandbox_verdicts',
    #detection---end

    #general --init
    'names',
    'signature_info',
    'import_list',
    #basic props --- init
    'md5',
    'sha1',
    'sha256',
    'type_description',
    'type_tags',
    'magin',
    'detectiteasy',
    'trid',
    'size',
    'packers',
    #basic props ---end
    #general --end
    
    #antivirus results --- init
    'last_analysis_results',
    #antivirus results --- end
)

# Estas tuplas se utilizan para la funcion ""
# This tuples is used to the functions ""

atrs_url = (
    #general---init
    'categories',
    'url',
    'last_final_url',
    'redirection_chain',
    'threat_names',
    #general---end
    #history----init
    'first_submission_date',
    'last_submission_date',
    'last_analysis_date',
    'last_modification_date',
    'times_submitted',
    #history----end
    #detection--init
    'tags',
    'total_votes',
    'last_analysis_stats',
    #detection--end
    #antivirus results --- init
    'last_analysis_results',
    #antivirus results --- end
)

