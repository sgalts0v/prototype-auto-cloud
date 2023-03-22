from enum import Enum
from dataclasses import dataclass


class TypeReport(Enum):
    Connection = 'Connections Report'


class AutomaticGeneration(Enum):
    Never = 'never'
    Daily = 'daily'


class Span(Enum):
    Month = 'month'


@dataclass
class Report:
    name: str
    automaticgeneration: AutomaticGeneration
    span: Span


connect_report = Report('Test Report', AutomaticGeneration.Never, Span.Month)
