def conecta():
    import lomadeepy
    app_token = '1605637282724491d653c'
    source_id = '36865079'
    loma=lomadeepy.lomadee(app_token,source_id)
    return loma
def loma_conecta():
    import lomadeepy
    categoria=lomadeepy.Categories.search(conecta())
    return(categoria)