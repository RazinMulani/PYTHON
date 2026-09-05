Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/connecctiviy.py =============
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/connecctiviy.py", line 1, in <module>
    from pymango import MangiClient
ModuleNotFoundError: No module named 'pymango'

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/connecctiviy.py =============
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/connecctiviy.py", line 1, in <module>
    from pymango import MongoClient
ModuleNotFoundError: No module named 'pymango'

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/connecctiviy.py =============
Conected Successfully

=============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_db.py ==============
Connected Successfully

=============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_db.py ==============
Connected Successfully

=============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_db.py ==============
Connected Successfully
Data Base Create Successfully

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_table.py =============
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_table.py", line 4, in <module>
    client = Mongoclient("mongodb://localhost:27017")
NameError: name 'Mongoclient' is not defined. Did you mean: 'MongoClient'?

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/create_table.py =============
Conected Successfully...!
Create Biodata Successfully....!
Collections Ready

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py", line 17, in <module>
    print("Inserted ID:",result.insert_id)
AttributeError: 'InsertOneResult' object has no attribute 'insert_id'. Did you mean: 'inserted_id'?

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Inserted ID: 6a32b3cf9e98ddb85e4ead22
Add Value Successfully

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py", line 16, in <module>
    result = collection.insert_one(employe)
NameError: name 'collection' is not defined. Did you mean: 'collections'?

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Inserted ID: 6a32b409f48d641bb8110f0f
InsertOneResult(ObjectId('6a32b409f48d641bb8110f0f'), acknowledged=True)
Add Value Successfully

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py", line 39, in <module>
    for result in find(employe):
NameError: name 'find' is not defined

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py", line 39, in <module>
    for data in collection.find():
NameError: name 'collection' is not defined. Did you mean: 'collections'?

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
{'_id': ObjectId('6a32b3a3bb7227b49dafecf5'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b3cf9e98ddb85e4ead22'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b409f48d641bb8110f0f'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
{'_id': ObjectId('6a32b3a3bb7227b49dafecf5'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b3cf9e98ddb85e4ead22'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b409f48d641bb8110f0f'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef2'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef3'), 'name': 'Sami', 'Emp-ID': 2, 'Emp-Salary': '2lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef4'), 'name': 'Shabnoor', 'Emp-ID': 3, 'Emp-Salary': '3lpa'}

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
InsertManyResult([ObjectId('6a32b598e3f4e8a996bde8a5'), ObjectId('6a32b598e3f4e8a996bde8a6'), ObjectId('6a32b598e3f4e8a996bde8a7')], acknowledged=True)

============== RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/add_values.py ==============
Conectted Successfully
InsertManyResult([ObjectId('6a32b5f3dd6b05333096a303'), ObjectId('6a32b5f3dd6b05333096a304'), ObjectId('6a32b5f3dd6b05333096a305')], acknowledged=True)
{'_id': ObjectId('6a32b3a3bb7227b49dafecf5'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b3cf9e98ddb85e4ead22'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b409f48d641bb8110f0f'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef2'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef3'), 'name': 'Sami', 'Emp-ID': 2, 'Emp-Salary': '2lpa'}
{'_id': ObjectId('6a32b573b5bc9116fe223ef4'), 'name': 'Shabnoor', 'Emp-ID': 3, 'Emp-Salary': '3lpa'}
{'_id': ObjectId('6a32b598e3f4e8a996bde8a5'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b598e3f4e8a996bde8a6'), 'name': 'Sami', 'Emp-ID': 2, 'Emp-Salary': '2lpa'}
{'_id': ObjectId('6a32b598e3f4e8a996bde8a7'), 'name': 'Shabnoor', 'Emp-ID': 3, 'Emp-Salary': '3lpa'}
{'_id': ObjectId('6a32b5f3dd6b05333096a303'), 'name': 'Razin', 'Emp-ID': 1, 'Emp-Salary': '1lpa'}
{'_id': ObjectId('6a32b5f3dd6b05333096a304'), 'name': 'Sami', 'Emp-ID': 2, 'Emp-Salary': '2lpa'}
{'_id': ObjectId('6a32b5f3dd6b05333096a305'), 'name': 'Shabnoor', 'Emp-ID': 3, 'Emp-Salary': '3lpa'}
Inserted ID's: [ObjectId('6a32b5f3dd6b05333096a303'), ObjectId('6a32b5f3dd6b05333096a304'), ObjectId('6a32b5f3dd6b05333096a305')]

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'gender': 'male', '_id': ObjectId('6a32b8af7ba14bce3d9b57ea')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'gender': 'male', '_id': ObjectId('6a32b8df4d077a2e95dfd3a7')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'gender': 'male', '_id': ObjectId('6a32b902f0c0cd3488dcabcb')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'Gender': 'male', '_id': ObjectId('6a32b96f6ddb525333e277e4')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'Gender': 'male', '_id': ObjectId('6a32ba40b8b7c2f2d0345274')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'Gender': 'male', '_id': ObjectId('6a32ba7eb3b5716b563dab27')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(students)
NameError: name 'students' is not defined. Did you mean: 'student'?

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
Traceback (most recent call last):
  File "C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py", line 27, in <module>
    result = collections.insert_many(student)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\_csot.py", line 125, in csot_wrapper
    return func(self, *args, **kwargs)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\collection.py", line 974, in insert_many
    blk.execute(write_concern, session, _Op.INSERT)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 751, in execute
    return self.execute_command(generator, write_concern, session, operation)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\synchronous\bulk.py", line 614, in execute_command
    _raise_bulk_write_error(full_result)
  File "C:\Users\razin\AppData\Roaming\Python\Python314\site-packages\pymongo\bulk_shared.py", line 131, in _raise_bulk_write_error
    raise BulkWriteError(full_result)
pymongo.errors.BulkWriteError: batch op errors occurred, full error: {'writeErrors': [{'index': 0, 'code': 13297, 'errmsg': 'db already exists with different case already have: [college] trying to create [College]', 'op': {'name': 'Razin', 'roll-no': 1, 'Gender': 'male', '_id': ObjectId('6a32babac5ba241b27338684')}}], 'writeConcernErrors': [], 'nInserted': 0, 'nUpserted': 0, 'nMatched': 0, 'nModified': 0, 'nRemoved': 0, 'upserted': []}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
{'_id': ObjectId('6a323160bcb5ea7be49d9ed2'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3232bc7b122ca040d1d13d'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a32337f75ae04934acea570'), 'age': 20, 'city': 'mahableshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a3236072f7550c69e048303'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3238718419b5f0e42d4054'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a3238718419b5f0e42d4055'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3238718419b5f0e42d4056'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a323910f7fe1439c3f666fe'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a323910f7fe1439c3f666ff'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a323910f7fe1439c3f66700'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a3239dde09bdf7787557541'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a3239dde09bdf7787557542'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3239dde09bdf7787557543'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a323b1d8675a380ce420980'), 'age': 24, 'city': 'Mahabaleshwar', 'email': 'shabnoor@gmail.com', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a323b1d8675a380ce420981'), 'age': 22, 'city': 'Mahabaleshwar', 'email': 'razin@gmail.com', 'student_name': 'razin'}
{'_id': ObjectId('6a323b1d8675a380ce420982'), 'age': 20, 'city': 'Mahabaleshwar', 'email': 'sami@gmail.com', 'student_name': 'sami'}
{'_id': ObjectId('6a32baf599424890f5d47652'), 'name': 'Razin', 'roll-no': 1, 'Gender': 'male'}
{'_id': ObjectId('6a32baf599424890f5d47653'), 'name': 'Sami', 'roll-no': 2, 'Gender': 'male'}
{'_id': ObjectId('6a32baf599424890f5d47654'), 'name': 'Shabnoor', 'roll-no': 3, 'Gender': 'male'}

============= RESTART: C:/Users/razin/OneDrive/Desktop/Core Python/CRUD/update_value.py =============
Connected Successfully
{'_id': ObjectId('6a323160bcb5ea7be49d9ed2'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3232bc7b122ca040d1d13d'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a32337f75ae04934acea570'), 'age': 20, 'city': 'mahableshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a3236072f7550c69e048303'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3238718419b5f0e42d4054'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a3238718419b5f0e42d4055'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3238718419b5f0e42d4056'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a323910f7fe1439c3f666fe'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a323910f7fe1439c3f666ff'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a323910f7fe1439c3f66700'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a3239dde09bdf7787557541'), 'age': 24, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a3239dde09bdf7787557542'), 'age': 22, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'razin'}
{'_id': ObjectId('6a3239dde09bdf7787557543'), 'age': 20, 'city': 'Mahabaleshwar', 'email': '', 'student_name': 'sami'}
{'_id': ObjectId('6a323b1d8675a380ce420980'), 'age': 24, 'city': 'Mahabaleshwar', 'email': 'shabnoor@gmail.com', 'student_name': 'Shabnoor'}
{'_id': ObjectId('6a323b1d8675a380ce420981'), 'age': 22, 'city': 'Mahabaleshwar', 'email': 'razin@gmail.com', 'student_name': 'razin'}
{'_id': ObjectId('6a323b1d8675a380ce420982'), 'age': 20, 'city': 'Mahabaleshwar', 'email': 'sami@gmail.com', 'student_name': 'sami'}
{'_id': ObjectId('6a32baf599424890f5d47652'), 'name': 'Razin', 'roll-no': 1, 'Gender': 'male'}
{'_id': ObjectId('6a32baf599424890f5d47653'), 'name': 'Sami', 'roll-no': 2, 'Gender': 'male'}
{'_id': ObjectId('6a32baf599424890f5d47654'), 'name': 'Shabnoor', 'roll-no': 3, 'Gender': 'female'}
{'_id': ObjectId('6a32bb0d3179cbe00e65b4ed'), 'name': 'Razin', 'roll-no': 1, 'Gender': 'male'}
{'_id': ObjectId('6a32bb0d3179cbe00e65b4ee'), 'name': 'Sami', 'roll-no': 2, 'Gender': 'male'}
{'_id': ObjectId('6a32bb0d3179cbe00e65b4ef'), 'name': 'Shabnoor', 'roll-no': 3, 'Gender': 'female'}
