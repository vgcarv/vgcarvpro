def lomaCredencial():
    from configparser import ConfigParser
    config = ConfigParser()
    config.read('application/EsteEuQuero/private/lomadee.ini')
    app_token = config.get('rest', 'app_token')
    source_id = config.get('rest', 'source_id') 
    return(app_token, source_id)