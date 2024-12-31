from model.Sql_Connection_Hoa import DatabaseConnection


class TongQuan_Model:
    def __init__(self, ):
        pass

    @staticmethod
    def get_quick_stats():
        """
        Lấy thông tin thống kê nhanh từ cơ sở dữ liệu.
        Trả về tổng số máu trong kho, tổng số người hiến, và số yêu cầu chưa xử lý.
        """
        db = DatabaseConnection()  # Tạo đối tượng kết nối cơ sở dữ liệu
        print(db)
        # Thống kê tổng số máu trong kho
        query_total_blood = """ SELECT SUM(Volume) FROM BloodInventory """
        result_total_blood = db.execute_query(query_total_blood)

        # Thống kê tổng số người hiến
        query_total_donors = """SELECT COUNT(*) FROM Donors"""
        result_total_donors = db.execute_query(query_total_donors)

        # Thống kê yêu cầu chưa xử lý
        query_pending_requests = """ SELECT COUNT(*) FROM Requests WHERE Status = N'Chờ xử lý' """
        result_pending_requests = db.execute_query(query_pending_requests)

        db.close()

        print(result_total_blood)
        print(result_total_donors)
        print(result_pending_requests)
        return {
            "total_blood": result_total_blood[0][0] if result_total_blood else 0,
            "total_donors": result_total_donors[0][0] if result_total_donors else 0,
            "pending_requests": result_pending_requests[0][0] if result_pending_requests else 0
        }
