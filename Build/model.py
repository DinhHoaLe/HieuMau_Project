class UserModel:
    def __init__(self, db):
        """Khởi tạo UserModel với đối tượng kết nối được truyền vào."""
        self.db = db

    def login(self, username, password):
        """Kiểm tra thông tin đăng nhập."""
        query = "SELECT * FROM Users WHERE username = ? AND password = ?"
        params = (username, password)
        result = self.db.execute_query(query, params)
        return result  # Trả về kết quả từ cơ sở dữ liệu
class BloodRequestModel:
    def __init__(self, db):
        self.db = db

    def get_all_requests(self):
        query = "SELECT RequestCode, PatientID, BloodType, RhFactor, VolumeRequested, RequestingDepartment, RequestDate, Status, Notes FROM Requests"
        return self.db.execute_query(query)

    def search_requests(self, search_term):
        query = """
            SELECT RequestCode, PatientID, BloodType, RhFactor, VolumeRequested, RequestingDepartment, RequestDate, Status, Notes
            FROM Requests
            WHERE RequestCode LIKE ? OR RequestingDepartment LIKE ?
        """
        return self.db.execute_query(query, [f"%{search_term}%"])

    def add_request(self, patient_name, blood_type, rh_factor, amount, department, request_date, status, notes):
        query = """
            INSERT INTO Requests (PatientID, BloodType, RhFactor, VolumeRequested, RequestingDepartment, RequestDate, Status, Notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_non_query(query, [patient_name, blood_type, rh_factor, amount, department, request_date, status, notes])

    def delete_request(self, request_code):
        query = "DELETE FROM Requests WHERE RequestCode = ?"
        self.db.execute_non_query(query, [request_code])
