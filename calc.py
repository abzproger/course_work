from abc import ABC, abstractmethod


class AbstractBankDeposit(ABC):
    def __init__(self, initial_deposit: float, p: float):
        self.__initial_deposit = initial_deposit
        self.__p = p / 100  # Преобразуем проценты в десятичную дробь

    @property
    def initial_deposit(self) -> float:
        return self.__initial_deposit

    @property
    def p(self) -> float:
        return self.__p

    @abstractmethod
    def calculate_time_to_reach_target(self, target_amount: float) -> tuple:
        pass


class BankDeposit(AbstractBankDeposit):
    def __init__(self, initial_deposit: float, p: float):
        super().__init__(initial_deposit, p)

    def calculate_time_to_reach_target(self, target_amount: float) -> tuple:
        if target_amount <= self.initial_deposit:
            raise ValueError("Целевая сумма должна быть больше начального вклада")

        months = 0
        deposit = self.initial_deposit

        try:
            while deposit < target_amount:
                deposit *= (1 + self.p)
                months += 1
        except OverflowError:
            raise OverflowError("Результат расчета превысил допустимый диапазон")

        return months, deposit
