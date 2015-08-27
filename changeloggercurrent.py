import datetime, getpass
import sublime, sublime_plugin


class ChangeloggercurrentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())
		# for region in allcontent:
		# rg = self.view.line(self.view.sel()[0])
		newrg = self.view.rowcol(self.view.size())
		# self.view.insert(edit, 0, "/**""\n""Task : Task Description""\n%s" %  datetime.datetime.now().strftime("%Y-%m-%d"))
		# self.view.sel().add(sublime.Region(rg.a,rg.b))
		# self.view.insert(edit, allcontent.end(), "\n""/**""\n""Task : Task Description""\n%s" "\n" "**/"%  datetime.datetime.now().strftime("%Y-%m-%d") )
		# { "keys": ["ctrl+end"], "command": "move_to", "args": {"to": "eof", "extend": "false"} }
		# self.view.run_command("go_to_line", {'line':'0'})
		self.view.run_command("go_to_line", {'line': newrg})
		
		self.view.run_command('insert_snippet',{'contents':'\n''/**''\n''Task : ${1:Task Description}''\n''Name : ${2:Your Name}''\n%s' '\n' '**/' %  datetime.datetime.now().strftime("%Y-%m-%d")})