from model.BaseModel import BaseModel

class Demo(BaseModel):
        
    # Tell here what is the primary key
    @property
    def __key__(that):
        return 'id'

    # Tell here what is the physic table name
    @property
    def __table__(that):
        return 'demonstration'

    # Tell here what are the table based model variables
    @property
    def __variables__(that):
        return ['id', 'name']