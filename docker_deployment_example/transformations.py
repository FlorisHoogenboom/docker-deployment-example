def drop_columns(data):
    return data[[
        'Air.Flow',
        'Water.Temp',
        'Acid.Conc.',
        'stack.loss'
    ]]

def rename_columns(data):
    return data.rename(columns={
        'Air.Flow': 'airFlow',
        'Water.Temp': 'waterTemp',
        'Acid.Conc.': 'acidConc',
        'stack.loss': 'target'
    })

def apply(data):
    data = drop_columns(data)
    data = rename_columns(data)
    return data