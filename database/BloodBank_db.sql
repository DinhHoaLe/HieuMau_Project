CREATE DATABASE BloodBank_db
COLLATE Vietnamese_CI_AS;

USE BloodBank_db;

-- Tạo bảng Bệnh nhân
CREATE TABLE Patients (
    PatientID INT IDENTITY(1,1) PRIMARY KEY, -- ID bệnh nhân
    PatientCode NVARCHAR(20) NULL, -- Mã bệnh nhân, cho phép NULL ban đầu
    FullName NVARCHAR(100) COLLATE Vietnamese_CI_AS NOT NULL, -- Tên bệnh nhân
    DateOfBirth DATE NOT NULL, -- Ngày sinh
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')), -- Giới tính
    BloodType NVARCHAR(3) CHECK (BloodType IN ('A', 'B', 'AB', 'O')), -- Nhóm máu
    RhFactor CHAR(1) CHECK (RhFactor IN ('+', '-')), -- Yếu tố Rh
    ContactNumber NVARCHAR(15), -- Số điện thoại
    Address NVARCHAR(200) COLLATE Vietnamese_CI_AS -- Địa chỉ
);
go
-- Trigger tự động tạo mã bệnh nhân
CREATE TRIGGER trg_GeneratePatientCode
ON Patients
AFTER INSERT
AS
BEGIN
    DECLARE @PatientID INT;
    -- Lấy PatientID từ bảng INSERTED
    SELECT @PatientID = PatientID FROM INSERTED;
    
    -- Cập nhật giá trị cho PatientCode
    UPDATE Patients
    SET PatientCode = 'PAT-' + FORMAT(@PatientID, '00000')
    WHERE PatientID = @PatientID;
END;
go
-- Tạo bảng Người hiến máu
CREATE TABLE Donors (
    DonorID INT IDENTITY(1,1) PRIMARY KEY, -- ID người hiến máu
    DonorCode NVARCHAR(20) NULL, -- Mã người hiến máu, cho phép NULL ban đầu
    FullName NVARCHAR(100) COLLATE Vietnamese_CI_AS NOT NULL, -- Tên người hiến máu
    DateOfBirth DATE NOT NULL, -- Ngày sinh
    Gender CHAR(1) CHECK (Gender IN ('M', 'F')), -- Giới tính
    BloodType NVARCHAR(3) CHECK (BloodType IN ('A', 'B', 'AB', 'O')), -- Nhóm máu
    RhFactor CHAR(1) CHECK (RhFactor IN ('+', '-')), -- Yếu tố Rh
    LastDonationDate DATE, -- Ngày hiến máu lần cuối
    ContactNumber NVARCHAR(15), -- Số điện thoại
    Address NVARCHAR(200) COLLATE Vietnamese_CI_AS -- Địa chỉ
);
go
-- Trigger tự động tạo mã người hiến máu
CREATE TRIGGER trg_GenerateDonorCode
ON Donors
AFTER INSERT
AS
BEGIN
    DECLARE @DonorID INT;
    -- Lấy DonorID từ bảng INSERTED
    SELECT @DonorID = DonorID FROM INSERTED;
    
    -- Cập nhật giá trị cho DonorCode
    UPDATE Donors
    SET DonorCode = 'DNR-' + FORMAT(@DonorID, '00000')
    WHERE DonorID = @DonorID;
END;
go
-- Tạo bảng Kho máu
CREATE TABLE BloodInventory (
    BloodID INT IDENTITY(1,1) PRIMARY KEY, -- ID đơn vị máu
    BloodCode NVARCHAR(20) NULL, -- Mã đơn vị máu, cho phép NULL ban đầu
    BloodType NVARCHAR(3) CHECK (BloodType IN ('A', 'B', 'AB', 'O')), -- Nhóm máu
    RhFactor CHAR(1)
	CHECK (RhFactor IN ('+', '-')), -- Yếu tố Rh
    Volume INT NOT NULL CHECK (Volume > 0), -- Lượng máu (ml)
    ExpirationDate DATE NOT NULL, -- Ngày hết hạn
    Source NVARCHAR(50) COLLATE Vietnamese_CI_AS DEFAULT 'Donation' -- Nguồn máu (hiến tặng)
);
go
-- Trigger tự động tạo mã đơn vị máu
CREATE TRIGGER trg_GenerateBloodCode
ON BloodInventory
AFTER INSERT
AS
BEGIN
    DECLARE @BloodID INT;
    -- Lấy BloodID từ bảng INSERTED
    SELECT @BloodID = BloodID FROM INSERTED;
    
    -- Cập nhật giá trị cho BloodCode
    UPDATE BloodInventory
    SET BloodCode = 'BLD-' + FORMAT(@BloodID, '00000')
    WHERE BloodID = @BloodID;
END;
go
-- Tạo bảng Yêu cầu máu
CREATE TABLE Requests (
    RequestID INT IDENTITY(1,1) PRIMARY KEY, -- ID yêu cầu
    RequestCode NVARCHAR(20) NULL, -- Mã yêu cầu máu, cho phép NULL ban đầu
    PatientID INT NULL, -- Khóa ngoại đến bảng Patients
    RequestingDepartment NVARCHAR(100) COLLATE Vietnamese_CI_AS NOT NULL, -- Khoa yêu cầu máu
    BloodType NVARCHAR(3) CHECK (BloodType IN ('A', 'B', 'AB', 'O')), -- Nhóm máu yêu cầu
    RhFactor CHAR(1) CHECK (RhFactor IN ('+', '-')), -- Yếu tố Rh yêu cầu
    VolumeRequested INT NOT NULL CHECK (VolumeRequested > 0), -- Lượng máu yêu cầu
    RequestDate DATE NOT NULL, -- Ngày yêu cầu
    Status NVARCHAR(50) CHECK (Status IN (N'Chờ xử lý', N'Đã hoàn thành', N'Đã từ chối')) DEFAULT N'Chờ xử lý', -- Trạng thái yêu cầu
    Notes NVARCHAR(MAX) COLLATE Vietnamese_CI_AS, -- Ghi chú
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE SET NULL
);
go
-- Trigger tự động tạo mã yêu cầu máu
CREATE TRIGGER trg_GenerateRequestCode
ON Requests
AFTER INSERT
AS
BEGIN
    DECLARE @RequestID INT;
    -- Lấy RequestID từ bảng INSERTED
    SELECT @RequestID = RequestID FROM INSERTED;
    
    -- Cập nhật giá trị cho RequestCode
    UPDATE Requests
    SET RequestCode = 'REQ-' + FORMAT(@RequestID, '00000')
    WHERE RequestID = @RequestID;
END;
go
-- Tạo bảng Lịch sử sử dụng máu của bệnh nhân
CREATE TABLE PatientBloodUsage (
    UsageID INT IDENTITY(1,1) PRIMARY KEY, -- ID lịch sử sử dụng máu
    UsageCode NVARCHAR(20) NULL, -- Mã lịch sử sử dụng máu, cho phép NULL ban đầu
    PatientID INT NOT NULL, -- Khóa ngoại đến bảng Patients
    BloodID INT NOT NULL, -- Khóa ngoại đến bảng BloodInventory
    UsageDate DATE NOT NULL, -- Ngày sử dụng máu
    BloodVolume INT NOT NULL CHECK (BloodVolume > 0), -- Lượng máu sử dụng
    DoctorNote NVARCHAR(MAX) COLLATE Vietnamese_CI_AS, -- Ghi chú của bác sĩ
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID) ON DELETE CASCADE,
    FOREIGN KEY (BloodID) REFERENCES BloodInventory(BloodID) ON DELETE CASCADE
);
go
-- Trigger tự động tạo mã lịch sử sử dụng máu
CREATE TRIGGER trg_GenerateUsageCode
ON PatientBloodUsage
AFTER INSERT
AS
BEGIN
    DECLARE @UsageID INT;
    -- Lấy UsageID từ bảng INSERTED
    SELECT @UsageID = UsageID FROM INSERTED;
    
    -- Cập nhật giá trị cho UsageCode
    UPDATE PatientBloodUsage
    SET UsageCode = 'USG-' + FORMAT(@UsageID, '00000')
    WHERE UsageID = @UsageID;
END;
go
-- Tạo bảng Lịch sử hiến máu
CREATE TABLE DonationRecords (
    RecordID INT IDENTITY(1,1) PRIMARY KEY, -- ID lịch sử hiến máu
    RecordCode NVARCHAR(20) NULL, -- Mã lịch sử hiến máu, cho phép NULL ban đầu
    DonorID INT NOT NULL, -- Khóa ngoại đến bảng Donors
    BloodID INT NOT NULL, -- Khóa ngoại đến bảng BloodInventory
    DonationDate DATE NOT NULL, -- Ngày hiến máu
    VolumeDonated INT NOT NULL CHECK (VolumeDonated > 0), -- Lượng máu hiến
    FOREIGN KEY (DonorID) REFERENCES Donors(DonorID) ON DELETE CASCADE,
    FOREIGN KEY (BloodID) REFERENCES BloodInventory(BloodID) ON DELETE CASCADE
);
go
-- Trigger tự động tạo mã lịch sử hiến máu
CREATE TRIGGER trg_GenerateRecordCode
ON DonationRecords
AFTER INSERT
AS
BEGIN
    DECLARE @RecordID INT;
    -- Lấy RecordID từ bảng INSERTED
    SELECT @RecordID = RecordID FROM INSERTED;
    
    -- Cập nhật giá trị cho RecordCode
    UPDATE DonationRecords
    SET RecordCode = 'DNR-' + FORMAT(@RecordID, '00000')
    WHERE RecordID = @RecordID;
END;

go
-- Test
--Thêm dữ liệu cho bảng Patients
INSERT INTO Patients (FullName, DateOfBirth, Gender, BloodType, RhFactor, ContactNumber, Address)
VALUES (N'Nguyễn Văn A', '1985-05-10', 'M', 'A', '+', '0987654321', N'123 Đường ABC, Hà Nội');
SELECT * FROM Patients;
--Thêm dữ liệu cho bảng Donors
INSERT INTO Donors (FullName, DateOfBirth, Gender, BloodType, RhFactor, LastDonationDate, ContactNumber, Address)
VALUES 
(N'Phạm Minh C', '1980-04-15', 'M', 'O', '+', '2024-06-01', '0987654323', N'789 Đường GHI, Hà Nội');
SELECT * FROM Donors;
--Thêm dữ liệu mẫu cho bảng BloodInventory
INSERT INTO BloodInventory (BloodType, RhFactor, Volume, ExpirationDate, Source)
VALUES 
('A', '+', 500, '2025-05-01', 'Donation');
SELECT * FROM BloodInventory;
--Thêm dữ liệu mẫu cho bảng Requests
INSERT INTO Requests (PatientID, RequestingDepartment, BloodType, RhFactor, VolumeRequested, RequestDate, Status)
VALUES 
(1, N'Khoa Hồi sức', 'A', '+', 300, '2024-12-01', N'Chờ xử lý');
SELECT * FROM Requests;
--Thêm dữ liệu mẫu cho bảng PatientBloodUsage
INSERT INTO PatientBloodUsage (PatientID, BloodID, UsageDate, BloodVolume, DoctorNote)
VALUES 
(1, 1, '2024-12-03', 300, N'Hiến máu cho bệnh nhân điều trị phẫu thuật');
SELECT * FROM PatientBloodUsage;
--Thêm dữ liệu mẫu cho bảng DonationRecords
INSERT INTO DonationRecords (DonorID, BloodID, DonationDate, VolumeDonated)
VALUES (1, 1, '2024-06-01', 500);
SELECT * FROM DonationRecords;


-----
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,      -- Mã người dùng
    Username NVARCHAR(50) UNIQUE NOT NULL,      -- Tên đăng nhập
    Password NVARCHAR(255) NOT NULL,            -- Mật khẩu (mã hóa)
    Role NVARCHAR(50) CHECK (Role IN ('Admin', 'Staff')) NOT NULL, -- Quyền (Admin hoặc Staff)
    Status NVARCHAR(20) CHECK (Status IN ('Active', 'Inactive')) DEFAULT 'Active' -- Trạng thái
);
-- Thêm người dùng Admin
INSERT INTO Users (Username, Password, Role, Status)
VALUES (N'admin', N'adminpassword', 'Admin', 'Active');
-- Thêm người dùng Staff
INSERT INTO Users (Username, Password, Role, Status)
VALUES (N'staff1', N'staffpassword', 'Staff', 'Active');