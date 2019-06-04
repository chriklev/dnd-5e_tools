#!/usr/bin/env python3
# encoding: utf-8

import npyscreen as nps


class ManualCharCreator(nps.ActionForm):
    def create(self):

        y, x = self.useable_space()
        gap = 1
        maxwidth = x//3-gap

        self.player_name = self.add(
            nps.TitleText,
            name='Player name:',
            max_width=maxwidth)
        self.character_name = self.add(
            nps.TitleText,
            name='Character name:',
            use_two_lines=False,
            max_width=maxwidth)
        self.level = self.add(
            nps.TitleSlider,
            name='Level',
            out_of=18,
            lowest=1,
            max_width=maxwidth)
        self.char_class = self.add(
            nps.TitleCombo,
            name='Class:',
            values=['Barbarian', 'Bard', 'Fighter'],
            max_width=maxwidth)
        self.race = self.add(
            nps.TitleCombo,
            name='Race',
            values=['Gnome', 'Dwarf', 'Elf', 'Human'],
            max_width=maxwidth)
        self.alignment = self.add(
            nps.TitleCombo,
            name='Alignment',
            values=[
                'Lawfull-Good', 'Lawfull-Neutral', 'Lawfull-Evil', 'Neutral-Good', 'Neutral-Neutral', 'Neutral-Evil', 'Chaotic-Good', 'Chaotic-Neutral', 'Chaotic-Evil'],
            max_width=maxwidth)
        self.background = self.add(
            nps.TitleCombo,
            name='Background',
            values=['Hermit', 'Nobel', 'Theif',
                    'noeannet', 'noemer', 'endamer'],
            max_width=maxwidth)
        self.max_hp = self.add(
            nps.TitleText,
            name='Max hit points',
            use_two_lines=False,
            max_width=maxwidth)
        self.poficiency_modifier = self.add(
            nps.TitleText,
            name='Proficiency bonus',
            use_two_lines=False,
            max_width=maxwidth)
        self.saving_throws = self.add(
            TitleMultiSelectBoxed,
            name='Saving throws',
            values=[
                'Strength', 'Dexterity', 'Constitution', 'Intelligense', 'Wisdom', 'Charisma'],
            scroll_exit=True,
            max_height=9,
            max_width=maxwidth,
            relx=x//3+gap,
            rely=1)
        self.skill_proficiencies = self.add(
            TitleMultiSelectBoxed,
            name='Skill proficiencies',
            values=[
                'asdf', 'asdfasd', 'asdfa', "qwerqew", "Acrobatics", "Animal handeling", "Arcana", "Athletics"],
            max_height=y-3,
            relx=2*(x//3+gap),
            rely=1)

    def afterEditing(self):
        pass

    def on_ok(self):
        nps.notify_confirm(
            "Character saved as *character name*.char", "Saved! B)", editw=1)
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        exiting = nps.notify_yes_no(
            "Are you sure you want to exit without saving?", "Don't leave me :'(", editw=1)
        if exiting:
            self.parentApp.setNextForm(None)


class TitleMultiSelectBoxed(nps.BoxTitle):
    _contained_widget = nps.MultiSelect


class CharTools(nps.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', ManualCharCreator,
                     name='Manual Character creator')


if __name__ == "__main__":
    app = CharTools()
    app.run()
