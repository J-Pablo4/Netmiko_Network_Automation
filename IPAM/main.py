import time
from fpdf import FPDF, XPos, YPos
from netmiko import ConnectHandler


class PDF(FPDF):
    def header(self):
        # logo
        self.image('Logo_del_ITESO.svg.png', 10, 8, 25)
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'Report', border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        self.ln(20)


# Create FPDF object
pdf = PDF('P', 'mm', 'Letter')

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# specify font
# fonts ()
pdf.set_font('helvetica', '', 16)

# Routers
r1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.60.163',
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
for i in range(1, 41):
    pdf.cell(0, 10, f'This is line {i} XD', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.output('pdf_1.pdf')
print("Report created successfully")

print("**Disconnecting**")
time.sleep(3)
# Disconnect from the device
net_connect.disconnect()
