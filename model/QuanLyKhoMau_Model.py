from model.Sql_Connection_Hoa import DatabaseConnection

class ImportInventory:
    def __init__(self, import_id=None, import_code=None, volume=None, import_date=None, source=None, blood_id=None):
        self.import_id = import_id
        self.import_code = import_code
        self.volume = volume
        self.import_date = import_date
        self.source = source
        self.blood_id = blood_id

    @staticmethod
    def add_import(volume=None, import_date=None, source=None, blood_id=None):
        """Thêm bản ghi nhập mới vào cơ sở dữ liệu và trả về ImportCode"""
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu
        query = """
                  INSERT INTO ImportInventory (Volume, ImportDate, Source, BloodId)
                    VALUES (?, ?, ?, ?);
                """
        params = (volume, import_date, source, blood_id)

        db.execute_query(query, params)  # Thực thi câu truy vấn và nhận kết quả
        db.commit()

        # Truy vấn lại ImportCode sau khi thêm bản ghi
        select_query = """
                    SELECT TOP 1 ImportCode
                    FROM ImportInventory
                    WHERE Volume = ? AND ImportDate = ? AND Source = ? AND BloodId = ?
                    ORDER BY ImportCode DESC;
                """
        select_params = (volume, import_date, source, blood_id)
        result = db.execute_query(select_query, select_params)  # Truy vấn ImportCode

        db.close()

        # Kiểm tra kết quả và lấy ImportCode
        if result:
            import_code = result[0][0]  # Lấy mã nhập kho từ kết quả truy vấn
            return import_code  # Trả về mã nhập kho
        else:
            return None  # Nếu không có kết quả, trả về None
    @staticmethod
    def get_list():
        """Lấy tất cả các bản ghi từ bảng ImportInventory"""
        db = DatabaseConnection()
        query = """
                SELECT ImportId, ImportCode, Volume, ImportDate, Source, BloodId
                FROM ImportInventory
            """

        # Thực thi câu truy vấn để lấy danh sách
        result = db.execute_query(query)
        # Nếu không có dữ liệu, trả về danh sách rỗng
        if not result:
            return []

        db.close()

        # Chuyển kết quả truy vấn thành danh sách các đối tượng ImportInventory
        import_list = []
        for row in result:
            import_obj = ImportInventory(
                import_id=row[0],
                import_code=row[1],
                volume=row[2],
                import_date=row[3],
                source=row[4],
                blood_id=row[5]
            )
            import_list.append(import_obj)

        return import_list
    @staticmethod
    def get_list_load_blood_entry_info():
        """Lấy thông tin hiển thị vào bảng thông tin nhập kho"""
        query = """
            SELECT a.ImportCode, b.BloodType, b.RhFactor, a.Volume, a.ImportDate, a.Source
            FROM ImportInventory a
            JOIN BloodInventory b ON a.BloodId = b.BloodId
        """

        db = DatabaseConnection()
        result = db.execute_query(query)
        db.close()
        # Kiểm tra kết quả trả về và tạo danh sách đối tượng ImportInventory
        list_load_blood_entry_info = []
        if result:
            for import_code, blood_type, rh_factor, volume, import_date, source in result:
                # Tạo đối tượng ImportInventory với các thuộc tính cần thiết
                entry = ImportInventory(import_code=import_code,
                                        volume= volume,
                                        import_date=import_date,
                                        source=source)
                # Thêm các thuộc tính từ BloodInventory vào đối tượng
                entry.blood_type = blood_type
                entry.rh_factor = rh_factor
                list_load_blood_entry_info.append(entry)
        else:
            return None  # Trả về None nếu không có dữ liệu

        return list_load_blood_entry_info
class BloodInventory:
    def __init__(self, blood_id=None, blood_type=None, rh_factor=None, volume=None):
        self.blood_id = blood_id
        self.blood_type = blood_type
        self.rh_factor = rh_factor
        self.volume = volume

    @staticmethod
    def get_blood_groups_stock():
        """Lấy thể thông tin tồn kho máu và trả về danh sách các nhóm máu và thể tích."""
        db = DatabaseConnection()
        query = """
                    SELECT BloodType, RhFactor, Volume
                    FROM BloodInventory
                """

        result = db.execute_query(query)
        db.close()

        # Kiểm tra kết quả trả về và tạo danh sách nhóm máu với thể tích
        blood_groups_stock = []
        if result:
            for blood_type, rh_factor, volume in result:
                blood_groups_stock.append((blood_type, rh_factor, volume))
        else:
            return None  # Trả về None nếu không có dữ liệu

        return blood_groups_stock

    @staticmethod
    def get_blood_id_by_type_and_rh(blood_type, rh_factor):
        """
        Lấy blood_id từ nhóm máu và yếu tố Rh.
        """
        db = DatabaseConnection()
        query = """
                    SELECT BloodId
                    FROM BloodInventory
                    WHERE BloodType = ? AND RhFactor = ?
                """

        result = db.execute_query(query, (blood_type, rh_factor))
        db.close()

        if result:
            return result[0][0]  # Trả về blood_id nếu tìm thấy
        return None  # Trả về None nếu không tìm thấy

    @staticmethod
    def check_blood_inventory(blood_id):
        """
        Kiểm tra tồn kho của một loại máu dựa trên BloodId.

        :param blood_id: ID của máu trong kho.
        :return: Số lượng máu hiện tại (ml) hoặc None nếu không tồn tại.
        """
        db = DatabaseConnection()

        query = """
            SELECT Volume
            FROM BloodInventory
            WHERE BloodId = ?
        """
        result = db.execute_query(query, (blood_id,))
        db.close()

        if result:
            return result[0][0]  # Trả về lượng máu hiện tại
        return None  # Không tồn tại BloodId

    @staticmethod
    def update_blood_volume(blood_id, volume_change):
        """
        Cập nhật số lượng máu trong kho dựa trên BloodId.
        Có thể cộng hoặc trừ lượng máu.

        :param blood_id: ID của máu trong kho.
        :param volume_change: Số lượng máu thay đổi (ml, có thể âm hoặc dương).
        """
        current_volume = BloodInventory.check_blood_inventory(blood_id)

        if current_volume is None:
            raise ValueError(f"BloodId {blood_id} không tồn tại trong kho.")

        # Chuyển đổi current_volume và volume_change sang kiểu số nếu cần
        current_volume = int (current_volume)
        volume_change = int (volume_change)

        new_volume = current_volume + volume_change

        # Đảm bảo volume không âm
        if new_volume < 0:
            raise ValueError(f"Không thể cập nhật vì lượng máu sẽ âm (BloodId: {blood_id}).")

        db = DatabaseConnection()
        query_update = """
            UPDATE BloodInventory
            SET Volume = ?
            WHERE BloodId = ?
        """
        db.execute_query(query_update, (new_volume, blood_id))
        db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        db.close()
class DonationRecords:
    def __init__(self, record_id=None, record_code=None, donation_id=None, import_code=None,donation_date=None, volume_donated=None):
        self.record_id = record_id
        self.record_code = record_code
        self.donation_id = donation_id
        self.import_code = import_code
        self.donation_date = donation_date
        self.volume_donated = volume_donated

    @staticmethod
    def add_record(donor_id=None, import_code=None, donation_date=None, volume_donated=None):
        """
        Thêm một bản ghi mới vào cơ sở dữ liệu trong bảng Donations.
        """
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu
        query = """
                INSERT INTO DonationRecords (DonorID, ImportCode, DonationDate, VolumeDonated)
                VALUES (?, ?, ?, ?)
            """
        params = (donor_id, import_code, donation_date, volume_donated)

        db.execute_query(query, params)  # Thực thi câu truy vấn với tham số
        db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
        db.close()  # Đóng kết nối

    @staticmethod
    def get_all_records():
        """
        Lấy tất cả các bản ghi từ bảng Donations.
        """
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu
        query = """
                SELECT RecordID, RecordCode, DonorID, ImportCode, DonationDate, VolumeDonated
                FROM DonationRecords
            """

        result = db.execute_query(query)  # Thực thi truy vấn
        records = result.fetchall()  # Lấy tất cả kết quả
        db.close()  # Đóng kết nối

        # Chuyển đổi kết quả thành danh sách dictionary
        data = []
        for row in records:
            data.append({
                "RecordID": row[0],
                "RecordCode": row[1],
                "DonorID": row[2],
                "ImportCode": row[3],
                "DonationDate": row[4],
                "VolumeDonated": row[5]
            })

        return data

    @staticmethod
    def get_blood_info(donor_code):
        """Lấy thông tin nhóm máu và yếu tố Rh theo mã người hiến"""
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu

        query = """
                    SELECT BloodType, RhFactor 
                    FROM Donors 
                    WHERE DonorCode = ?
                """
        result = db.execute_query(query, (donor_code,))  # Truy vấn với tham số

        db.close()  # Đóng kết nối
        # Kiểm tra kết quả và trả về thông tin
        return {"blood_type": result[0][0], "rh_factor": result[0][1]} if result else None

    @staticmethod
    def get_donor_id_by_code(donor_code):
        """
        Tìm ID của người hiến máu thông qua mã DonorCode.
        """
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu

        query = """
                    SELECT DonorID
                    FROM Donors
                    WHERE DonorCode = ?
                """
        result = db.execute_query(query, (donor_code,))  # Truy vấn với tham số

        db.close()  # Đóng kết nối

        # Kiểm tra kết quả và trả về DonorID
        return result[0][0] if result else None