class Cell:
    def __init__(self, element: Element):
        self.element = element
        self.input = self.element.element('input')

    def start_editing(self):
        self.element.double_click()
        return self

    def set(self, value):
        self.input.set_value(value)
        return self

    def save(self):
        self.input.press_enter()
        return self


class Row:
    def __init__(self, container: Element):
        self.container = container
        self.cells = container.all('td')

    def cell(self, number):
        index = number - 1
        return Cell(self.cells[index])

    def remove(self):
        self.container.element('.remove').click()
        return self


class Table:
    # def __init__(self, container: str):
    #     self.container = browser.element('#employees')
    def __init__(self, container: Element):
        self.container = container
        self.rows = self.container.all('[role=rowgroup]')

    def row(self, number):
        index = number - 1
        return Row(self.rows[index])

    def add(self):
        self.container.element('.table-add').click()
        return Row(self.rows[-1])

# modal_dialog = browser.element('.modal-dialog')
# employees = Table('#table')
employees = Table(browser.element('#table'))
employees.row(1).cell(2).start_editing().set('John').save()
employees.row(2).remove()
employees.add().cell(3).start_editing().set('QA').save()
