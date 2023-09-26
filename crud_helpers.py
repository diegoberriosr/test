from fastapi import HTTPException, status
def get_all(model, db, name):
    all = db.query(model).all()

    if len(all) == 0:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail={'ERROR' : f'no {name} in database'})
    
    return all

def get_by_id(model, db, id, name):
    
    match = db.query(model).filter_by(id=id).first()

    if not match:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail={'ERROR' : f'{name} with id={id} not found'})

    return match


def delete_by_id(model, db, id):
    db.query(model).filter_by(id=id).delete()
    db.commit()