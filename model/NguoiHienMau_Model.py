from model.Sql_Connection_Hoa import DatabaseConnection

class DonorModel:
    def __init__(self, donor_id,donor_code, full_name,DOB,gender, blood_type, rh_factor, last_donation_date, phone, address):
        self.donor_id = donor_id
        self.donor_code = donor_code
        self.full_name = full_name
        self.DOB = DOB
        self.blood_type = blood_type
        self.rh_factor = rh_factor
        self.gender = gender
        self.last_donation_date = last_donation_date
        self.phone = phone
        self.address = address

    @staticmethod
    def get_all_donor():
        db = DatabaseConnection()
        query = "SELECT * FROM Donors"
        result = db.execute_query(query)
        db.close()
        return result

    @staticmethod
    def search_donor(search_term):
        db = DatabaseConnection()
        query = "SELECT * FROM Donors WHERE DonorCode LIKE ? OR FullName LIKE ?"
        result = db.execute_query(query, ('%' + search_term + '%', '%' + search_term + '%'))
        db.close()
        return result

    @staticmethod
    def add_donor(request):
        db = DatabaseConnection()
        query = """INSERT INTO Donors (patient_name, blood_type, rh_factor, blood_amount, department, request_date, status, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        db.execute_query(query, (request.patient_name, request.blood_type, request.rh_factor, request.blood_amount, request.department, request.request_date, request.status, request.notes))
        db.commit()
        db.close()

    @staticmethod
    def delete_donor(request_id):
        db = DatabaseConnection()
        query = "DELETE FROM Donors WHERE DonorID = ?"  # Sử dụng DonorID
        try:
            db.execute_query(query, (request_id,))
            db.commit()
            print(f"✅ Người hiến máu với ID={request_id} đã được xóa.")
        except Exception as e:
            print(f"❌ Lỗi khi xóa người hiến máu: {e}")
        finally:
            db.close()


