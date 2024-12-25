from model.NguoiHienMau_Model import DonorModel
from model.Sql_Connection_Hoa import DatabaseConnection


def test_query():
    try:
        db = DatabaseConnection()
        print("✅ Kết nối cơ sở dữ liệu thành công!")

        # Thực thi truy vấn kiểm tra
        query = "SELECT COUNT(*) FROM Donors"
        result = db.execute_query(query)
        print(f"🔍 Số lượng người hiến máu trong bảng Donors: {result[0][0]}")

        db.close()
    except Exception as e:
        print(f"❌ Lỗi khi thực thi truy vấn: {e}")


if __name__ == '__main__':
    test_query()
