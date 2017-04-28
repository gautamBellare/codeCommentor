import datetime, getpass
import sublime, sublime_plugin


class ChangeloggerCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(self.view.size(), self.view.size())
		newrg = self.view.rowcol(self.view.size())
		self.view.sel().clear()
		self.view.sel().add(allcontent)
		self.view.run_command('insert_snippet',{'contents':'\n''/**''\n''Task : ${1:Task Description}''\n''Name : ${2:Your Name}''\n%s' '\n' '**/' %  datetime.datetime.now().strftime("%Y-%m-%d")})
