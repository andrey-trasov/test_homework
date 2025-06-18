

class ReportData:

    def __init__(self, title, content):
        self.title = title
        self.content = content


class ReportGenerator:

    def generate_pdf(self):
        print("PDF generated")


class ReportStorage:

    def save_to_file(self, filename):
        print(f"Saved {filename}")

