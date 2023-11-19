import time
from fpdf import FPDF, XPos, YPos
from netmiko import ConnectHandler

title = "IPAM Report"


class PDF(FPDF):
    def header(self):
        # logo
        self.image('Logo_del_ITESO.svg.png', 10, 8, 25)
        self.set_font('helvetica', 'B', 20)
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.cell(title_w, 10, title, border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(10)

    # page footer
    def footer(self):
        # Set position of footer
        self.set_y(-15)
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(169, 169, 169)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

    def router_number_title(self, r_num):
        self.set_font('helvetica', 'B', 12)
        self.set_fill_color(200, 220, 225)
        router_title = f'Router {r_num} Interfaces>'
        # self.cell(0, 10, ' ', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln()
        self.cell(0, 5, router_title, new_x=XPos.LMARGIN, new_y=YPos.NEXT, fill=True)
        self.ln()

    def body(self, text):
        self.set_font('helvetica', '', 12)
        self.multi_cell(0, 8, text, align='J')
        self.ln()

    def print_router_int(self, r_num, text):
        self.add_page()
        self.router_number_title(r_num)
        self.body(text)


# Create FPDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Routers
r1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.60.165',
    'username': 'netadmin',
    'password': 'Passw0rd'
}

net_connect = ConnectHandler(**r1)
print("**Successfully Connected**\n")
time.sleep(3)
print("Router 1 Interfaces>")
time.sleep(2)
sh_output = net_connect.send_command("show ip int brief")
print(sh_output)
time.sleep(2)
# Add text
# w = width
# h = height


pdf.print_router_int(1, sh_output)

pdf.output('pdf_1.pdf')
print("Report created successfully")

print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
