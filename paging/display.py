
class PageList:
    def __init__(self, current_page, total_pages):
        self.current_page = current_page
        self.total_pages = total_pages

    def display(self):
        def write_page(page_number):
            output = ''
            if page_number == self.current_page:
                output = f'({page_number})'
            else:
                output = f'{page_number}'
            return output

        out = ''
        if self.total_pages >= 1:
            out += write_page(1)
        for page in range(2, self.total_pages + 1):
            out += ' ' + write_page(page)
        return out
