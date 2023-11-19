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
    'host': '3.3.0.34',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r2 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.6',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r3 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.2',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r4 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.10',
    'username': 'netadmin',
    'password': 'Passw0rd'
}
r5 = {
    'device_type': 'cisco_ios',
    'host': '3.3.0.13',
    'username': 'netadmin',
    'password': 'Passw0rd'
}


# Router 1
net_connect = ConnectHandler(**r1)
print("**Successfully Connected to Router 1**\n")
time.sleep(1)
print("**Gathering All Router 1 Interface Information**")
time.sleep(1)
print("Router 1 Interfaces>")
time.sleep(1)
sh_output = net_connect.send_command("show ip int brief")
print(sh_output)
time.sleep(1)

# Router 2
net_connect = ConnectHandler(**r2)
print("**Successfully Connected to Router 2**\n")
time.sleep(1)
print("**Gathering All Router 2 Interface Information**")
time.sleep(1)
print("Router 2 Interfaces>")
time.sleep(1)
sh_output2 = net_connect.send_command("show ip int brief")
print(sh_output2)
time.sleep(1)

# Router 3
net_connect = ConnectHandler(**r3)
print("**Successfully Connected to Router 3**\n")
time.sleep(1)
print("**Gathering All Router 3 Interface Information**")
time.sleep(1)
print("Router 3 Interfaces>")
time.sleep(1)
sh_output3 = net_connect.send_command("show ip int brief")
print(sh_output3)
time.sleep(1)

# Router 4
net_connect = ConnectHandler(**r4)
print("**Successfully Connected to Router 4**\n")
time.sleep(1)
print("**Gathering All Router 4 Interface Information**")
time.sleep(1)
print("Router 4 Interfaces>")
time.sleep(1)
sh_output4 = net_connect.send_command("show ip int brief")
print(sh_output4)
time.sleep(1)

# Router 5
net_connect = ConnectHandler(**r5)
print("**Successfully Connected to Router 5**\n")
time.sleep(1)
print("**Gathering All Router 5 Interface Information**")
time.sleep(1)
print("Router 5 Interfaces>")
time.sleep(1)
sh_output5 = net_connect.send_command("show ip int brief")
print(sh_output5)
time.sleep(1)

# Add text
# w = width
# h = height

print("**Creating PDF Report**")
time.sleep(1)
pdf.print_router_int(1, sh_output)
pdf.print_router_int(2, sh_output2)
pdf.print_router_int(3, sh_output3)
pdf.print_router_int(4, sh_output4)
pdf.print_router_int(5, sh_output5)


pdf.output('ipam_report.pdf')
print("**Report Created Successfully**")
time.sleep(1)
print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
