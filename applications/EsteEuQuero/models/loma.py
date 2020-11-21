def lomaCredencial():
    #Buscar configuracao na pasta private
    import os
    fp = os.path.join(request.folder,'private','lomadee.ini')   
    # 
    #Abre arquivo formato .ini e busca parametros
    from configparser import ConfigParser
    config = ConfigParser()
    config.read(fp)
    app_token = config.get('rest', 'app_token')
    source_id = config.get('rest', 'source_id') 
    return(app_token, source_id)