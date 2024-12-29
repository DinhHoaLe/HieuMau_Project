from model.Sql_Connection_Hoa import DatabaseConnection


class BloodRequest:
    def __init__(self, request_id, request_code, patient_id, request_department, blood_type, rh_factor, volume_request,
                 request_date, status, notes):
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
        # query = "SELECT * FROM Requests"
        query = """
               SELECT 
                   RQ.RequestID,
                   PT.PatientID, 
                   PT.FullName, 
                   RQ.BloodType, 
                   RQ.RhFactor, 
                   RQ.VolumeRequested, 
                   RQ.RequestingDepartment, 
                   RQ.RequestDate, 
                   RQ.Status, 
                   RQ.Notes
               FROM 
                   REQUESTS RQ
               JOIN 
                   PATIENTS PT 
               ON 
                   RQ.PatientID = PT.PatientID
               """

        result = db.execute_query(query)
        db.close()
        return result

    @staticmethod
    def get_request_by_id(request_id):
        db = DatabaseConnection()
        query = "SELECT PatientID, RequestingDepartment, BloodType, RhFactor, VolumeRequested, RequestDate, Status, Notes FROM Requests WHERE RequestID = ?"
        result = db.execute_query(query, (request_id,))
        db.close()
        if result:
            return result[0]
        else:
            print("Không có dữ liệu trả về từ database.")
            return None

    @staticmethod
    def search_requests(search_term):
        db = DatabaseConnection()
        query = "SELECT * FROM blood_requests WHERE patient_name LIKE ?"
        result = db.execute_query(query, ('%' + search_term + '%',))
        db.close()
        return result

    @staticmethod
    def add_request(request):
        print(request)
        db = DatabaseConnection()
        query = """INSERT INTO Requests (PatientID, RequestingDepartment, BloodType, RhFactor, VolumeRequested, RequestDate, Status, Notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            db.execute_query(query, (
                request.get('Mã bệnh nhân'),
                request.get('Khoa yêu cầu'),
                request.get('Nhóm máu'),
                request.get('Yếu tố Rh'),
                request.get('Lượng máu'),
                request.get('Ngày yêu cầu'),
                request.get('Trạng thái'),
                request.get('Ghi chú')
            ))
            db.commit()
            print("✅ Thêm yêu cầu máu thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi thêm yêu cầu máu: {e}")
        finally:
            db.close()

    @staticmethod
    def update_request_by_id(request_id, request_data):
        """Cập nhật thông tin người hiến máu trong CSDL."""
        db = DatabaseConnection()
        query = """
            UPDATE Requests
            SET 
                PatientID = ?,
                RequestingDepartment = ?,
                BloodType = ?,
                RhFactor = ?,
                VolumeRequested = ?,
                RequestDate = ?,
                Status = ?,
                Notes = ?
            WHERE RequestID = ?;
        """
        try:
            db.execute_query(query, (
                request_data.get("Mã bệnh nhân"),
                request_data.get("Khoa yêu cầu"),
                request_data.get("Nhóm máu"),
                request_data.get("Yếu tố Rh"),
                request_data.get("Lượng máu"),
                request_data.get("Ngày yêu cầu"),
                request_data.get("Trạng thái"),
                request_data.get("Ghi chú"),
                request_id
            ))
            db.commit()
            print("✅ Thông tin yêu cầu hiến máu đã được cập nhật thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật thông tin yêu cầu hiến máu: {e}")
            raise e
        finally:
            db.close()

    @staticmethod
    def delete_request(request_id):
        db = DatabaseConnection()
        query = "DELETE FROM Requests WHERE RequestID = ?"
        db.execute_query(query, (request_id,))
        db.commit()
        db.close()

    @staticmethod
    def search_requests_by_patient(search_term):
        """Tìm kiếm thông tin yêu cầu hiến máu theo mã bệnh nhân hoặc tên bệnh nhân."""
        db = DatabaseConnection()
        query = """
                SELECT * FROM requests
                WHERE patientid LIKE ? OR patientname LIKE ?
                """
        try:
            result = db.execute_query(query, ('%' + search_term + '%', '%' + search_term + '%'))

            # Thông báo tìm thấy kết quả
            print("✅ Thông tin yêu cầu hiến máu được tìm thấy")

            return result
        except Exception as e:
            print(f"❌ Lỗi tìm kiếm thông tin yêu cầu hiến máu: {e}")
            raise e
        finally:
            db.close()  # Đảm bảo đóng kết nối sau khi truy vấn xong


