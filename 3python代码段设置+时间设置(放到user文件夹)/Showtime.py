import datetime
import sublime, sublime_plugin
class AddAuthorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", 
            { 
                "contents": 
"# -*- coding: utf-8 -*-\n\
# @Author   : Sdite\n\
# @DateTime : %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),     
            } 
            )