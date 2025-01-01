from model.Sql_Connection_Hoa import DatabaseConnection


class TongQuan_Model:
    @staticmethod
    def get_quick_stats():
        """
        Lấy thông tin thống kê nhanh từ cơ sở dữ liệu.
        Trả về tổng số máu trong kho, tổng số người hiến, và số yêu cầu chưa xử lý.
        """
        db = DatabaseConnection()
        try:
            # Thực hiện nhiều truy vấn trong cùng một kết nối
            queries = {
                "total_blood": """SELECT SUM(Volume) FROM BloodInventory""",
                "total_donors": """SELECT COUNT(*) FROM Donors""",
                "pending_requests": """SELECT COUNT(*) FROM Requests WHERE Status = N'Chờ xử lý'"""
            }
            results = {}
            for key, query in queries.items():
                result = db.execute_query(query)
                results[key] = result[0][0] if result else 0

            return results
        except Exception as e:
            print(f"Lỗi trong get_quick_stats: {e}")
            return {"total_blood": 0, "total_donors": 0, "pending_requests": 0}
        finally:
            db.close()

    @staticmethod
    def get_blood_groups_stock():
        """
        Lấy tồn kho nhóm máu từ cơ sở dữ liệu.
        """
        db = DatabaseConnection()
        try:
            query = """SELECT BloodType, RhFactor, SUM(Volume) 
                       FROM BloodInventory 
                       GROUP BY BloodType, RhFactor"""
            result = db.execute_query(query)

<<<<<<< Updated upstream
            # Chuyển kết quả thành danh sách
            blood_groups = [(row[0], row[1], row[2]) for row in result]
            return blood_groups
        except Exception as e:
            print(f"Lỗi trong get_blood_groups_stock: {e}")
            return []
        finally:
            db.close()
    #commit
=======
        db.close()

        return {
            "total_blood": result_total_blood[0][0] if result_total_blood else 0,
            "total_donors": result_total_donors[0][0] if result_total_donors else 0,
            "pending_requests": result_pending_requests[0][0] if result_pending_requests else 0
        }
>>>>>>> Stashed changes
