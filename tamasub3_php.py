import sublime, sublime_plugin, re

#===================================================================================
#
# INIT Vars
# 
#===================================================================================
class Php_initvarsCommand(sublime_plugin.TextCommand):
	
	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				for row in rows:
					if row != "":
						str += re.sub(r'^','$',row) + ' = "";\n'
					else:
						str += "\n"
				
				#remove end of \n
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

#===================================================================================
#
# $_GET[]
# 
#===================================================================================
class Php_getparamsCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				for row in rows:
					if row != "":
						str += "if(isset($_GET['" + row + "'])) " + re.sub(r'^','$',row) + " = htmlspecialchars($_GET['" + row + "']);\n"
					else:
						str += "\n"
				
				#remove end of \n
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

#===================================================================================
#
# $_POST[]
# 
#===================================================================================
class Php_postparams(sublime_plugin.TextCommand):
	
	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				for row in rows:
					if row != "":
						str += "if(isset($_POST['" + row + "'])) " + re.sub(r'^','$',row) + " = htmlspecialchars($_POST['" + row + "']);\n"
					else:
						str += "\n"
				
				#remove end of \n
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

#===================================================================================
#
# GET COOKIE
# 
#===================================================================================
class Php_getcookie(sublime_plugin.TextCommand):

	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				for row in rows:
					if row != "":
						str += "if(isset($_COOKIE['" + row + "'])) $" + row + " = $_COOKIE['" + row + "'];\n"
					else:
						str += "\n"
				
				#remove end of \n
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

#===================================================================================
#
# SET COOKIE
# 
#===================================================================================
class Php_setcookieCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				for row in rows:
					if row != "":
						str += "setcookie('" + row + "',$" + row + ");\n"
					else:
						str += "\n"
				
				#remove end of \n
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

#===================================================================================
#
# SET foreach loop
# 
#===================================================================================
class Php_foreachCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		#get selected region
		for region in self.view.sel():

			if region.empty():

				sublime.message_dialog('Please select lines.')

			else :

				#get region
				selected = self.view.substr(region)

				#split by \n
				rows = selected.split('\n');

				str = ""
				str += "foreach($stmt->fetchAll(PDO::FETCH_ASSOC) as $row){\n\n"
				for row in rows:
					if row != "":
						str += "\t$" + row + " = $row['" + row + "'];\n"
					else:
						str += "\n"
				
				#remove end of \n
				str += "\n}\n"
				str = str.rstrip()

				#replace region by str
				self.view.replace(edit, region, str)

