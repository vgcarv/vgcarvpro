def lomaCredencial():
    import os
    fp = os.path.join(request.folder,'private','lomadee.ini')    
    from configparser import ConfigParser
    config = ConfigParser()
    config.read(fp)
    app_token = config.get('rest', 'app_token')
    source_id = config.get('rest', 'source_id') 
    return(app_token, source_id)