from controller.NguoiHIenMau_Controller import DonorBloodController
from controller.YeuCauMau_Controller import BloodRequestController
from controller.TongQuan_Controller import StatisticalController
from view.App_View import AppView


class AppController:
    def __init__(self, root):
        self.view = AppView(root, self)

        controller = DonorBloodController(root)
        controller = BloodRequestController(root)
        controller = StatisticalController(root)
