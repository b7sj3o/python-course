from .. import api
from .. models import Employee 

@api.get('/employee', response_model=Employee)
def read_employee():
    return Employee(
        name='Jamal',
        requirements=['clean', 'sort products', 'protect products'],
        salary=19200
    )
