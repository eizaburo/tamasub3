import sublime, sublime_plugin

#===================================================================================
#
# CREATE TABLE
# 
#===================================================================================
class Sql_createtableCommand(sublime_plugin.WindowCommand):

	def run(self):

		#input panel
		self.window.show_input_panel("Input TABLE NAME: ","",self.on_done,None,None)

	#callback
	def on_done(self,word):

		if word != "":

			#call other class with parameter.
			self.window.run_command("sql_createtable_sub",{"word":word})

		#when input is empty word.
		else:

			sublime.message_dialog("Please input text.")


#sub class
class Sql_createtable_subCommand(sublime_plugin.TextCommand):

	def run(self,edit,word):

		#get the selected area.
		select_area = self.view.sel()

		#loop in selected area.
		for region in select_area:

			#if no selected
			if region.empty():

				sublime.message_dialog("Plase select area.")

			#if multiple area selected.
			elif len(select_area) >= 2:

				sublime.message_dialog("Plase select one area.")

			else:

				#get selected area
				area = self.view.substr(region)

				#split by row.
				rows = area.split('\n')

				_str = ""
				_str = "DROP TABLE IF EXISTS " + word + ";\n"
				_str = "CREATE TABLE " + word + "(\n"

				#loop in rows.
				for row in rows:

					_str += "\t" + row.replace("\t"," ").rstrip() + ",\n"

				else:

					#remove ",\n"
					_str = _str.rstrip(",\n")
					#add \n);
					_str += "\n);"
				
				#replace building strings.
				self.view.replace(edit, region, _str)

		else:

			pass
			#sublime.message_dialog(_str)

#===================================================================================
#
# INSERT
# 
#===================================================================================
class Sql_insertCommand(sublime_plugin.WindowCommand):

	def run(self):

		#input panel
		self.window.show_input_panel("Input TABLE NAME: ","",self.on_done,None,None)

	#callback
	def on_done(self,word):

		if word != "":

			#call other class with parameter.
			self.window.run_command("sql_insert_sub",{"word":word})

		#when input is empty word.
		else:

			sublime.message_dialog("Please input text.")


#sub class
class Sql_insert_subCommand(sublime_plugin.TextCommand):

	def run(self,edit,word):

		#get the selected area.
		select_area = self.view.sel()

		#loop in selected area.
		for region in select_area:

			#if no selected
			if region.empty():

				sublime.message_dialog("Plase select area.")

			#if multiple area selected.
			elif len(select_area) >= 2:

				sublime.message_dialog("Plase select one area.")

			else:

				#get selected area
				area = self.view.substr(region)

				#split by row.
				rows = area.split('\n')

				#building SQL
				_str = '$stmt = $dbh->prepare("INSERT INTO ' + word + '(\n'
					
				#split by row.
				#add columns
				for row in rows:
					_str += "\t" + row + ",\n"
				else:
					_str = _str.rstrip(',\n')
					_str += "\n) VALUES(\n"

				#values
				for row in rows:
					_str += "\t:" + row + ",\n"
				else:
					_str = _str.rstrip(',\n')
					_str += "\n)\");"

				#add return
				_str += "\n\n"

				#add bindPrams
				for row in rows:
					_str += '$stmt->bindParam(":' + row + '", $' + row + ');\n' 

				#add execute
				_str += "\n"
				_str += "$stmt->execute();"


				#replace region by _str
				self.view.replace(edit, region, _str)

		else:

			pass
			#sublime.message_dialog(_str)


#===================================================================================
#
# Update
# 
#===================================================================================
class Sql_updateCommand(sublime_plugin.WindowCommand):

	def run(self):

		#input panel
		self.window.show_input_panel("Input TABLE NAME: ","",self.on_done,None,None)

	#callback
	def on_done(self,word):

		if word != "":

			#call other class with parameter.
			self.window.run_command("sql_update_sub",{"word":word})

		#when input is empty word.
		else:

			sublime.message_dialog("Please input text.")


#sub class
class Sql_update_subCommand(sublime_plugin.TextCommand):

	def run(self,edit,word):

		#get the selected area.
		select_area = self.view.sel()

		#loop in selected area.
		for region in select_area:

			#if no selected
			if region.empty():

				sublime.message_dialog("Plase select area.")

			#if multiple area selected.
			elif len(select_area) >= 2:

				sublime.message_dialog("Plase select one area.")

			else:

				#get selected area
				area = self.view.substr(region)

				#split by row.
				rows = area.split('\n')

				#building SQL
				str = '$stmt = $dbh->prepare("UPDATE ' + word + ' SET \n'
			
				#column
				for row in rows:
					str += "\t" + row + " = :" + row + ",\n"
				else:
					str = str.rstrip(',\n')
					str += ' \nWHERE id = :id");'

				#
				str += "\n\n"

				#bind
				for row in rows:
					str += '$stmt->bindParam(":' + row + '", $' + row + ');\n'
				else:
					str += '$stmt->bindParam(":id",$id);\n'


				#execute
				str += "\n"
				str += "$stmt->execute();"

				#replace region by str
				self.view.replace(edit, region, str)

		else:

			pass
			#sublime.message_dialog(_str)

