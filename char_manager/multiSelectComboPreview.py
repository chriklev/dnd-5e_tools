#!/usr/bin/env python3

import npyscreen as nps


class MultiSelectComboPreview(nps.ComboBox):

    def __init__(self, screen, *args, **kwargs):
        self.text = kwargs['text']
        super().__init__(screen, *args, **kwargs)

    def _print(self):
        if self.value == None or self.value is '':
            printme = '-unset-'
        else:
            try:
                printme = self.display_value(
                    [self.values[i] for i in self.value])
            except IndexError:
                printme = '-error-'
        if self.do_colors():
            self.parent.curses_pad.addnstr(
                self.rely, self.relx, printme, self.width, self.parent.theme_manager.findPair(self))
        else:
            self.parent.curses_pad.addnstr(
                self.rely, self.relx, printme, self.width)

    def h_change_value(self, input):
        F = PopupWidgetPreview(
            name=self.name,
            values=[self.display_value(x) for x in self.values],
            value=self.value,
            text=self.text)
        F.display()
        F.editWidget()
        self.value = F.getValue()


class TitleMultiSelectComboPreview(nps.TitleCombo):
    _entry_type = MultiSelectComboPreview


class PopupWidgetPreview(nps.Form):
    DEFAULT_LINES = 16
    DEFAULT_COLUMNS = 80
    SHOW_ATX = 5
    SHOW_ATY = 2

    def __init__(self, *args, **kwargs):
        #self.x = self.useable_space()[1]
        self.values = kwargs['values']
        self.value = kwargs['value']
        self.text = kwargs['text']
        super().__init__(*args, **kwargs)

    def create(self):
        x = self.useable_space()[1]
        seperation = x//3

        self.selection_widget = self.add(
            MultiSelectPreview,
            values=self.values,
            value=self.value,
            max_width=seperation-1,
            form_object=self)

        self.text = [self.splitString(s, x - seperation - 4)
                     for s in self.text]

        self.preview_widget = self.add(
            nps.Pager,
            # self.text[0].split('\n'),
            values=[
                "123456789112345678921234567893123456789412345678951234567896123456789"],
            relx=seperation+1,
            rely=1)

    def splitString(self, s, width):
        lines = [""]
        for w in s.split(' '):
            if len(lines[-1] + ' ' + w) > width:
                lines.append(w)
            else:
                lines[-1] += ' ' + w
        return lines

    def editWidget(self):
        self.selection_widget.edit()

    def updatePreview(self):
        self.preview_widget.values = self.text[self.selection_widget.cursor_line]
        self.preview_widget.update()

    def getValue(self):
        return self.selection_widget.value


class MultiSelectPreview(nps.MultiSelect):
    def __init__(self, screen, *args, **kwargs):
        self.form_object = kwargs['form_object']
        super().__init__(screen, *args, **kwargs)

    def h_cursor_line_down(self, ch):
        super().h_cursor_line_down(ch)
        self.form_object.updatePreview()

    def h_cursor_line_up(self, ch):
        super().h_cursor_line_up(ch)
        self.form_object.updatePreview()
