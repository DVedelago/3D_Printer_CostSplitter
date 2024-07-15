""" 


Defining the Research lines between which the costs must be split. 
using [Data_Structure] to assign Users to PIs


"""
# ################################################
# class ResearchLine:                            
                                               
#     def __init__(self, owners[], cm3) -> None: 
#         self.owners = owners[]                 
#         self.cm3_usage = cm3                   

# ################################################



# hhcm_owners = [
#     'Akash_Singh',
#     'aksingh',
#     'cburchielli',
#     'edb',
#     'ggarofalo',
#     'Giovanni_Garofalo',
#     'gsofia',
#     'Ioannis_Sarakoglou',
#     'Jorn_Malzahn',
#     'LBaccelliere',
#     'Navvab',
#     'Pietro_Gurnari',
#     'scarrozzo',
#     'Yifan',
#     'yizhang'
# ]



#HHCM_Tsagarakis = ResearchLine(hhcm_owners, 0)

###############################################################################################################################################

HHCM_Tsagarakis = {
    'owners': [
        'Akash_Singh',
        'aksingh',
        'cburchielli',
        'edb',
        'ggarofalo',
        'Giovanni_Garofalo',
        'gsofia',
        'Ioannis_Sarakoglou',
        'Jiang',
        'Jorn_Malzahn',
        'LBaccelliere',
        'Navvab',
        'Pietro_Gurnari',
        'pgurnari',
        'scarrozzo',
        'Yifan',
        'yizhang'
    ],
    'total_cm3': 0,
    'res_line_name': "HHCM Tsagarakis"
}


ADVR_Caldwell = {
    'owners': [
        'alperen_acemoglu',
        'asantangelo',
        'cabello',
        'Carola_Abello',
        'Carlo_Rizzardo',
        'cdinatali',
        'DPARK',
        'Federico_Mariano',
        'federico_allione',
        'fnozadheravi',
        'Farshad_NH',
        'Jesús_Ortiz',
        'JOrtiz',
        'ksawant',
        'lorenzo_ceppari',
        'msposito',
        'mlahoud',
        'psencandan',
        'rgagliardi',
        'Roberto_Pitzalis',
        'rpitzalis',
        'yonas tefera',
        'Yaesol_kim'
    ],
    'total_cm3': 0,
    'res_line_name': "ADVR Caldwell"
}

ADVRF_Cordasco = {
    'owners': [
        'Yussef_Hassanien',
        'dvedelago',
        'mmigliorini',
        '--'                    # cadbottle, axis calib and maintenance prints
    ],
    'total_cm3': 0,
    'res_line_name': "ADVRF Cordasco"
}

DLS_Semini = {
    'owners': [
        'Giacomo_Mazzaglia',
        'Victor_Barasuol',
        'VBarasuol',
        'Sinan_Emre',
        'Matteo_Villa',
        'mavilla',
        'semre',
        'Seyed_Amir_Mohamad_Hosseini_Rad',
        'isabe'
    ],
    'total_cm3': 0,
    'res_line_name': "DLS Semini"
}

HRII_Ajoudani = {
    'owners': [
        'Robin_Arbaud',
        'Fran_Ruiz',
        'pbalatti',
        'ggiardini',
        'Mattia_Leonori',
        'Pietro_Balatti',
        'fruiz',
        'rarbaud'
    ],
    'total_cm3': 0,
    'res_line_name': "HRII Ajoudani"

}

IRF_Canali = {
    'owners':[
        'Iacopo_Longinotti',
        'carlo_canali',
        'CCanali',
        'Lizhou_Xu',
        'khelifa_baizid',
        'ardit_poka',
        'federico_manara'
    ],
    'total_cm3': 0,
    'res_line_name': "IRF Canali"
}



res_lines_list = [
    IRF_Canali,
    HRII_Ajoudani,
    DLS_Semini,
    ADVRF_Cordasco,
    ADVR_Caldwell,
    HHCM_Tsagarakis
]
