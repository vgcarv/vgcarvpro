def conecta():
    app_token = '1605637282724491d653c'
    source_id = '36865079'
    import lomadeepy
    loma = lomadeepy.Lomadee(app_token, source_id)
    categoria=lomadeepy.Categories.all(loma)
    return(categoria)