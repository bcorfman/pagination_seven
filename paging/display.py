
class Pages:
    def __init__(self, **kwargs):
        self.selected_page = kwargs['selected']
        if kwargs['total'] < 1:
            raise OutOfRangeException('ERROR: total pages < 1')
        self.total_pages = kwargs['total']

    def display(self):
        def format_page_number(p):
            selected_page_number = f'({p})'
            regular_page_number = f'{p}'
            return selected_page_number if p == self.selected_page else regular_page_number

        def shorten_list(pages):
            if len(pages) > 7:
                if self.selected_page in range(1, 5):
                    pages = [f'{p}' for i, p in enumerate(pages) if i + 1 < 6] + ['...', f'{self.total_pages}']
                elif self.selected_page in range(self.total_pages - 3, self.total_pages + 1):
                    pages = ['1', '...'] + [p for i, p in enumerate(pages) if i + 1 > self.total_pages - 5]
                else:
                    pages = ['1', '...'] + [p for i, p in enumerate(pages)
                                            if self.selected_page - 1 <= i+1 <=  self.selected_page + 1] + \
                            ['...', f'{self.total_pages}']
            return pages

        formatted_pages = shorten_list([format_page_number(p) for p in range(1, self.total_pages+1)])
        return ' '.join(formatted_pages)
