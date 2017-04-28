import datetime, getpass
import sublime, sublime_plugin


class ChangeloggercurrentCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())
		newrg = self.view.rowcol(self.view.size())
		self.view.run_command("go_to_line", {'line': newrg})
		self.view.run_command('insert_snippet',{'contents':'\n''/**''\n''Task : ${1:Task Description}''\n''Name : ${2:Your Name}''\n%s' '\n' '**/' %  datetime.datetime.now().strftime("%Y-%m-%d")})
