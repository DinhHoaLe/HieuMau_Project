USE [master]
GO
/****** Object:  Database [BloodBank_db]    Script Date: 12/12/2024 10:26:12 PM ******/
CREATE DATABASE [BloodBank_db]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'BloodBank_db', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\BloodBank_db.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'BloodBank_db_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\BloodBank_db_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [BloodBank_db] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [BloodBank_db].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [BloodBank_db] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [BloodBank_db] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [BloodBank_db] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [BloodBank_db] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [BloodBank_db] SET ARITHABORT OFF 
GO
ALTER DATABASE [BloodBank_db] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [BloodBank_db] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [BloodBank_db] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [BloodBank_db] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [BloodBank_db] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [BloodBank_db] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [BloodBank_db] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [BloodBank_db] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [BloodBank_db] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [BloodBank_db] SET  ENABLE_BROKER 
GO
ALTER DATABASE [BloodBank_db] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [BloodBank_db] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [BloodBank_db] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [BloodBank_db] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [BloodBank_db] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [BloodBank_db] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [BloodBank_db] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [BloodBank_db] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [BloodBank_db] SET  MULTI_USER 
GO
ALTER DATABASE [BloodBank_db] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [BloodBank_db] SET DB_CHAINING OFF 
GO
ALTER DATABASE [BloodBank_db] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [BloodBank_db] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [BloodBank_db] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [BloodBank_db] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [BloodBank_db] SET QUERY_STORE = ON
GO
ALTER DATABASE [BloodBank_db] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [BloodBank_db]
GO
/****** Object:  Table [dbo].[BloodInventory]    Script Date: 12/12/2024 10:26:12 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BloodInventory](
	[BloodID] [int] IDENTITY(1,1) NOT NULL,
	[BloodCode] [nvarchar](20) NULL,
	[BloodType] [nvarchar](3) NULL,
	[RhFactor] [char](1) NULL,
	[Volume] [int] NOT NULL,
	[ExpirationDate] [date] NOT NULL,
	[Source] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[BloodID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DonationRecords]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DonationRecords](
	[RecordID] [int] IDENTITY(1,1) NOT NULL,
	[RecordCode] [nvarchar](20) NULL,
	[DonorID] [int] NOT NULL,
	[BloodID] [int] NOT NULL,
	[DonationDate] [date] NOT NULL,
	[VolumeDonated] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[RecordID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Donors]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Donors](
	[DonorID] [int] IDENTITY(1,1) NOT NULL,
	[DonorCode] [nvarchar](20) NULL,
	[FullName] [nvarchar](100) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[Gender] [char](1) NULL,
	[BloodType] [nvarchar](3) NULL,
	[RhFactor] [char](1) NULL,
	[LastDonationDate] [date] NULL,
	[ContactNumber] [nvarchar](15) NULL,
	[Address] [nvarchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[DonorID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PatientBloodUsage]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PatientBloodUsage](
	[UsageID] [int] IDENTITY(1,1) NOT NULL,
	[UsageCode] [nvarchar](20) NULL,
	[PatientID] [int] NOT NULL,
	[BloodID] [int] NOT NULL,
	[UsageDate] [date] NOT NULL,
	[BloodVolume] [int] NOT NULL,
	[DoctorNote] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[UsageID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Patients]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Patients](
	[PatientID] [int] IDENTITY(1,1) NOT NULL,
	[PatientCode] [nvarchar](20) NULL,
	[FullName] [nvarchar](100) NOT NULL,
	[DateOfBirth] [date] NOT NULL,
	[Gender] [char](1) NULL,
	[BloodType] [nvarchar](3) NULL,
	[RhFactor] [char](1) NULL,
	[ContactNumber] [nvarchar](15) NULL,
	[Address] [nvarchar](200) NULL,
PRIMARY KEY CLUSTERED 
(
	[PatientID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Requests]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Requests](
	[RequestID] [int] IDENTITY(1,1) NOT NULL,
	[RequestCode] [nvarchar](20) NULL,
	[PatientID] [int] NULL,
	[RequestingDepartment] [nvarchar](100) NOT NULL,
	[BloodType] [nvarchar](3) NULL,
	[RhFactor] [char](1) NULL,
	[VolumeRequested] [int] NOT NULL,
	[RequestDate] [date] NOT NULL,
	[Status] [nvarchar](50) NULL,
	[Notes] [nvarchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[RequestID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Users]    Script Date: 12/12/2024 10:26:13 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Users](
	[UserID] [int] IDENTITY(1,1) NOT NULL,
	[Username] [nvarchar](50) NOT NULL,
	[Password] [nvarchar](255) NOT NULL,
	[Role] [nvarchar](50) NOT NULL,
	[Status] [nvarchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[UserID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[Username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[BloodInventory] ADD  DEFAULT ('Donation') FOR [Source]
GO
ALTER TABLE [dbo].[Requests] ADD  DEFAULT (N'Chờ xử lý') FOR [Status]
GO
ALTER TABLE [dbo].[Users] ADD  DEFAULT ('Active') FOR [Status]
GO
ALTER TABLE [dbo].[DonationRecords]  WITH CHECK ADD FOREIGN KEY([BloodID])
REFERENCES [dbo].[BloodInventory] ([BloodID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[DonationRecords]  WITH CHECK ADD FOREIGN KEY([DonorID])
REFERENCES [dbo].[Donors] ([DonorID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[PatientBloodUsage]  WITH CHECK ADD FOREIGN KEY([BloodID])
REFERENCES [dbo].[BloodInventory] ([BloodID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[PatientBloodUsage]  WITH CHECK ADD FOREIGN KEY([PatientID])
REFERENCES [dbo].[Patients] ([PatientID])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[Requests]  WITH CHECK ADD FOREIGN KEY([PatientID])
REFERENCES [dbo].[Patients] ([PatientID])
ON DELETE SET NULL
GO
ALTER TABLE [dbo].[BloodInventory]  WITH CHECK ADD CHECK  (([BloodType]='O' OR [BloodType]='AB' OR [BloodType]='B' OR [BloodType]='A'))
GO
ALTER TABLE [dbo].[BloodInventory]  WITH CHECK ADD CHECK  (([RhFactor]='-' OR [RhFactor]='+'))
GO
ALTER TABLE [dbo].[BloodInventory]  WITH CHECK ADD CHECK  (([Volume]>(0)))
GO
ALTER TABLE [dbo].[DonationRecords]  WITH CHECK ADD CHECK  (([VolumeDonated]>(0)))
GO
ALTER TABLE [dbo].[Donors]  WITH CHECK ADD CHECK  (([BloodType]='O' OR [BloodType]='AB' OR [BloodType]='B' OR [BloodType]='A'))
GO
ALTER TABLE [dbo].[Donors]  WITH CHECK ADD CHECK  (([Gender]='F' OR [Gender]='M'))
GO
ALTER TABLE [dbo].[Donors]  WITH CHECK ADD CHECK  (([RhFactor]='-' OR [RhFactor]='+'))
GO
ALTER TABLE [dbo].[PatientBloodUsage]  WITH CHECK ADD CHECK  (([BloodVolume]>(0)))
GO
ALTER TABLE [dbo].[Patients]  WITH CHECK ADD CHECK  (([BloodType]='O' OR [BloodType]='AB' OR [BloodType]='B' OR [BloodType]='A'))
GO
ALTER TABLE [dbo].[Patients]  WITH CHECK ADD CHECK  (([Gender]='F' OR [Gender]='M'))
GO
ALTER TABLE [dbo].[Patients]  WITH CHECK ADD CHECK  (([RhFactor]='-' OR [RhFactor]='+'))
GO
ALTER TABLE [dbo].[Requests]  WITH CHECK ADD CHECK  (([BloodType]='O' OR [BloodType]='AB' OR [BloodType]='B' OR [BloodType]='A'))
GO
ALTER TABLE [dbo].[Requests]  WITH CHECK ADD CHECK  (([RhFactor]='-' OR [RhFactor]='+'))
GO
ALTER TABLE [dbo].[Requests]  WITH CHECK ADD CHECK  (([Status]=N'Đã từ chối' OR [Status]=N'Đã hoàn thành' OR [Status]=N'Chờ xử lý'))
GO
ALTER TABLE [dbo].[Requests]  WITH CHECK ADD CHECK  (([VolumeRequested]>(0)))
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD CHECK  (([Role]='Staff' OR [Role]='Admin'))
GO
ALTER TABLE [dbo].[Users]  WITH CHECK ADD CHECK  (([Status]='Inactive' OR [Status]='Active'))
GO
USE [master]
GO
ALTER DATABASE [BloodBank_db] SET  READ_WRITE 
GO
