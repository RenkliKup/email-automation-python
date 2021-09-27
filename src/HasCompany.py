from sql import CompanyDb

def hasCompany(receiver):
    db=CompanyDb()
    db.createTable()
    if len(db.hasCompany(receiver))==0:
        db.insert(receiver)
        print("oldu")
        return True
    else:
        return False

