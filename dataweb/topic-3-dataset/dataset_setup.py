import dataset

db = dataset.connect('sqlite:///shopping_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Sundeep' },
        { "description": 'Gaddam' },
        { "description": 'Rohith' },
        { "description": 'Vishal' },
        { "description": 'Ganesh' }
        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()