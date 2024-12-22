from abc import ABC, abstractmethod

# Abstract Person Class
class AbstractPerson(ABC):
    def __init__(self, id, name, dob, blood_type, rh_factor, phone, address):
        self._id = id
        self._name = name
        self._dob = dob
        self._blood_type = blood_type
        self._rh_factor = rh_factor
        self._phone = phone
        self._address = address

    @abstractmethod
    def get_info(self):
        pass


# Patient Class
class Patient(AbstractPerson):
    def __init__(self, id, name, dob, blood_type, rh_factor, phone, address):
        super().__init__(id, name, dob, blood_type, rh_factor, phone, address)

    def get_info(self):
        return f"Patient {self._name}, Blood Group: {self._blood_type}"


# Donor Class
class Donor(AbstractPerson):
    def __init__(self, id, name, dob, blood_type, rh_factor, phone, address, last_donation_date):
        super().__init__(id, name, dob, blood_type, rh_factor, phone, address)
        self._last_donation_date = last_donation_date

    def get_info(self):
        return f"Donor {self._name}, Last Donation: {self._last_donation_date}"

    def donate_blood(self, volume):
        print(f"Donor {self._name} has donated {volume} ml of blood.")


# Blood Inventory Class
class BloodInventory:
    def __init__(self):
        self.inventory = {}

    def add_blood(self, blood_id, blood_type, rh_factor, volume, expiry_date, source):
        self.inventory[blood_id] = {"Blood type": blood_type, "RH Factor": rh_factor, "Volume": volume,
                                    "Expiry Date": expiry_date, "Source": source}
        print(f"Blood {blood_id} added to inventory.")

    def update_blood(self, blood_id, new_volume):
        if blood_id in self.inventory:
            self.inventory[blood_id]["Volume"] = new_volume
            print(f"Blood {blood_id} updated with new volume: {new_volume} ml.")
        else:
            print(f"Blood ID {blood_id} not found.")

    def delete_blood(self, blood_id):
        if blood_id in self.inventory:
            del self.inventory[blood_id]
            print(f"Blood {blood_id} removed from inventory.")
        else:
            print(f"Blood ID {blood_id} not found.")

    def check_availability(self, blood_type, required_volume):
        for blood_id, details in self.inventory.items():
            if details["Blood type"] == blood_type and details["Volume"] >= required_volume:
                return True
        return False


# Request Class
class Request:
    def __init__(self):
        self.requests = []

    def create_request(self, request_id, blood_type, volume, request_date, status):
        self.requests.append({"Request ID": request_id, "Blood type": blood_type,
                              "Volume": volume, "Request Date": request_date, "Status": status})
        print(f"Request {request_id} created.")

    def update_status(self, request_id, new_status):
        for req in self.requests:
            if req["Request ID"] == request_id:
                req["Status"] = new_status
                print(f"Request {request_id} updated to {new_status}.")
                return
        print(f"Request ID {request_id} not found.")

    def delete_request(self, request_id):
        for req in self.requests:
            if req["Request ID"] == request_id:
                self.requests.remove(req)
                print(f"Request {request_id} deleted.")
                return
        print(f"Request ID {request_id} not found.")


# Main function
if __name__ == "__main__":
    # Tạo đối tượng bệnh nhân và người hiến máu
    patient_1 = Patient("P001", "Như", "1996-01-01", "B+", "123", "0111111111", "123 Street")
    patient_2 = Patient("P002", "Nhi", "1999-01-01", "O+", "124", "022222222", "124 Street")
    donor_1 = Donor("D001", "Hòa", "1995-05-05", "O+", "+", "987654321", "456 Avenue", "2024-01-01")
    donor_2 = Donor("D002", "Ai đó", "1980-05-05", "O+", "+", "987654320", "457 Avenue", "2024-12-01")

    print("\n--- Patient and Donor Info ---")
    print(patient_1.get_info())
    print(patient_2.get_info())
    print(donor_1.get_info())
    print(donor_2.get_info())

    # Quản lý kho máu
    blood_inventory = BloodInventory()
    blood_inventory.add_blood("B001", "O+", "+", 1000, "2025-01-01", "Hospital")
    blood_inventory.add_blood("B002", "A+", "-", 800, "2024-12-31", "Clinic")
    blood_inventory.update_blood("B001", 1200)  # Cập nhật kho máu
    print("Blood Availability (O+, 500ml):", "Available" if blood_inventory.check_availability("O+", 500) else "Not Available")
    blood_inventory.delete_blood("B002")  # Xóa nhóm máu

    # Quản lý yêu cầu máu
    blood_request = Request()
    blood_request.create_request("R001", "O+", 500, "2024-12-15", "Pending")
    blood_request.update_status("R001", "Completed")
    blood_request.delete_request("R001")  # Xóa yêu cầu

    # Donor hiến máu
    donor_1.donate_blood(500)
    donor_2.donate_blood(250)
