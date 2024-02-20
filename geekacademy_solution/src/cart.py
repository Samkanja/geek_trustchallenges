# from src.models import Program
from src.program_charges import ProgramCharges
from typing import Tuple
from src.models import check_matches


class Cart:
    def __init__(self) -> None:
        self.programs_lst = []
        self.programs_count = []
        self.programs_cost = []
        self.coupon_discount = 0
        self.pro_enrollement = True
        self.pro_discount = 0
        self.enrollment_fee = 0

    def add_program(self, program, qty):
        price = getattr(ProgramCharges, program)
        self.programs_cost.append(price)
        self.programs_lst.append(program)
        self.programs_count.append(qty)

    def print_bill(self) -> None:
        print(f"total cost for each program  {self.total()}")
        print(f"dispay total pro enrollemnt discount {self.pro_memberShip_dis()}")
        print(f"display client if has pro membership {self.has_pro_enroll()}")
        print(f"if client charge enrollment fee {self.get_enrollement_fee()}")
        print(f"new total with deduction {self.new_total()}")
        print(f"Due total of the whole program {self.due()}")

    def total(self) -> float:
        program_total = 0
        for i, ele in enumerate(self.programs_cost):
            program_total += ele * self.programs_count[i]
        return program_total

    def pro_memberShip_dis(self):

        if self.pro_enrollement:

            pro_dis, pro_discount = 0, 0

            for i, ele in enumerate(self.programs_lst):
                match ele:
                    case "CERTIFICATION":
                        pro_dis = self.programs_cost[i] * 2 / 100
                    case "DEGREE":
                        pro_dis = self.programs_cost[i] * 3 / 100
                    case "DIPLOMA":
                        pro_dis = self.programs_cost[i] * 1 / 100
                pro_discount += pro_dis * self.programs_count[i]
            return pro_discount

    def get_enrollement_fee(self):
        return 500 if self.total() < 6666 else 0

    def has_pro_enroll(self):

        return 200 if self.pro_enrollement else 0

    def new_total(self):
        return (
            self.total() + self.has_pro_enroll() + self.get_enrollement_fee()
        ) - self.pro_memberShip_dis()

    def has_coupon(self, coupon):

        if sum(self.programs_count) > 4 and coupon == "B4G1":
            self.coupon_discount = min(self.programs_cost)
        if self.new_total() > 10000 and coupon == "DEAL_G20":
            self.coupon_discount = self.new_total() * 2 / 100
        if sum(self.programs_count) > 2:
            self.coupon_discount = self.new_total() * 5 / 100

    def due(self):
        return self.new_total() - self.coupon_discount
