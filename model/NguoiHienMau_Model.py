from model.Sql_Connection_Hoa import DatabaseConnection


class DonorModel:
    def __init__(self, donor_id, donor_code, full_name, DOB, gender, blood_type, rh_factor, last_donation_date, phone,
                 address):
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
    def get_donor_by_id(donor_id):
        db = DatabaseConnection()
        query = "SELECT * FROM Donors WHERE DonorID = ?"
        result = db.execute_query(query, (donor_id,))
        db.close()
        if result:
            return result[0]
        else:
            print("Không có dữ liệu trả về từ database.")
            return None

    @staticmethod
    def update_donor_by_id(donor_id, donor_data):
        """Cập nhật thông tin người hiến máu trong CSDL."""
        db = DatabaseConnection()
        query = """
            UPDATE Donors
            SET 
                DonorCode = ?,
                FullName = ?,
                DateOfBirth = ?,
                Gender = ?,
                BloodType = ?,
                RhFactor = ?,
                LastDonationDate = ?,
                ContactNumber = ?,
                Address = ?
            WHERE DonorID = ?;
        """
        try:
            print("🛠️ Thực thi truy vấn cập nhật với dữ liệu sau:")
            print(donor_data)
            db.execute_query(query, (
                donor_data.get("Mã máu"),
                donor_data.get("Họ và tên"),
                donor_data.get("Sinh nhật"),
                donor_data.get("Giới tính"),
                donor_data.get("Nhóm máu"),
                donor_data.get("Yếu tố Rh"),
                donor_data.get("Ngày hiến gần nhất"),
                donor_data.get("Điện thoại"),
                donor_data.get("Địa chỉ"),
                donor_id
            ))
            db.commit()
            print("✅ Thông tin người hiến máu đã được cập nhật thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi cập nhật thông tin người hiến máu: {e}")
            raise e
        finally:
            db.close()

    @staticmethod
    def search_donor(search_term):
        db = DatabaseConnection()
        query = "SELECT * FROM Donors WHERE DonorID LIKE ? OR FullName LIKE ?"
        result = db.execute_query(query, ('%' + search_term + '%', '%' + search_term + '%'))
        db.close()
        return result

    @staticmethod
    def add_donor(donor_data):
        db = DatabaseConnection()
        query = """
            INSERT INTO Donors (
                FullName, DateOfBirth, Gender, BloodType, RhFactor, 
                LastDonationDate, ContactNumber, Address
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            db.execute_query(query, (
                donor_data.get('Họ và tên'),
                donor_data.get('Sinh nhật'),
                donor_data.get('Giới tính'),
                donor_data.get('Nhóm máu'),
                donor_data.get('Yếu tố Rh'),
                donor_data.get('Ngày hiến gần nhất'),
                donor_data.get('Điện thoại'),
                donor_data.get('Địa chỉ')
            ))
            db.commit()
            print("✅ Thêm người hiến máu thành công!")
        except Exception as e:
            print(f"❌ Lỗi khi thêm người hiến máu: {e}")
        finally:
            db.close()

    @staticmethod
    def delete_donor_by_id(request_id):
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
