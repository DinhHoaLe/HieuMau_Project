from model.Sql_Connection import DatabaseConnection

class BloodRequest:
    def __init__(self, request_id,request_code, patient_id,request_department,blood_type, rh_factor, volume_request, request_date, status, notes):
        self.request_id = request_id
        self.request_code = request_code
        self.patient_id = patient_id
        self.request_department = request_department
        self.blood_type = blood_type
        self.rh_factor = rh_factor
        self.volume_request = volume_request
        self.request_date = request_date
        self.status = status
        self.notes = notes

    @staticmethod
    def get_all_requests():
        db = DatabaseConnection()
        query = "SELECT * FROM Requests"
        result = db.execute_query(query)
        db.close()
        return result

    @staticmethod
    def search_requests(search_term):
        db = DatabaseConnection()
        query = "SELECT * FROM blood_requests WHERE patient_name LIKE ?"
        result = db.execute_query(query, ('%' + search_term + '%',))
        db.close()
        return result

    @staticmethod
    def add_request(request):
        db = DatabaseConnection()
        query = """INSERT INTO blood_requests (patient_name, blood_type, rh_factor, blood_amount, department, request_date, status, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        db.execute_query(query, (request.patient_name, request.blood_type, request.rh_factor, request.blood_amount, request.department, request.request_date, request.status, request.notes))
        db.commit()
        db.close()

    @staticmethod
    def delete_request(request_id):
        db = DatabaseConnection()
        query = "DELETE FROM blood_requests WHERE id = ?"
        db.execute_query(query, (request_id,))
        db.commit()
        db.close()
