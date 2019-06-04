#!/usr/bin/env python3
# encoding: utf-8

import npyscreen as nps
from multiSelectComboPreview import MultiSelectComboPreview, TitleMultiSelectComboPreview


class ManualCharCreator(nps.ActionForm):
    def create(self):

        y, x = self.useable_space()
        gap = 1
        maxwidth = x//3-gap

        Options = nps.OptionList()
        options = Options.options

        options.append(
            nps.OptionMultiChoice(
                'Saving throws',
                choices=[
                    'Strength', 'Dexterity', 'Constitution', 'Intelligense', 'Wisdom', 'Charisma'],
                short_explanation='Dette er en kort beskrivelse! hei'))

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
            nps.OptionListDisplay,
            name="Saving Throws",
            values=options,
            scroll_exit=True,
            max_height=2)
        self.skill_proficiencies = self.add(
            TitleMultiSelectComboPreview,
            name='Skill proficiencies',
            values=[
                'asdf', 'asdfasd', 'asdfa', "qwerqew", "Acrobatics", "Animal handeling", "Arcana", "Athletics"],
            text=[
                'asdf hei', 'asdfasd alsdkbføa', 'asdfa asdøkfjb', "qwerqew kafdkajsdøkjansdøfkjnaslkdjfbnlkajdbsflkjadbsflkjadbsf", "Acrobatics aksdjbfi apsijdnfajsdf jasdjfna jdasdofjna dojfadjfajds aojd nfao jndf jansdjfao jsasdojfja aojdsfjasdf ajodsfajos asdofn aojsdfoa aodsjfn oajdfojadsfjona aojdf aojdf\nPOADJFN JADF ADJFN\najdsnfoaj\nasodjasdojfnafd asdf ads. Hvordan går det med deg? Når jeg ser ut i det store universet tenker jeg på aper. Hvordan kan aper åpne en banen men en stein kan ikke fly? tre ting er like tregt som en pappflaske; elver, tanker og tid. Når to foreldre møtes skaper de en alternativ tidslinje hvor livet ikke suger. Jeg kan noe som ikke du kan. Jeg kan danse opera. Er du sjalu på min opera? *danser på spansk* Hvor mange penaler trenger man for å åpne en kopp? Linken! For slavene svømmer ikke av seg selv. Det hadde vært fint med selvsvømmende slaver. kanskje vi får noe sånt en gang i framtiden, men for nå må vi klare oss med pisking.", "Animal handeling o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o o 0 0 0 o o o o o po j g k g l t n i   j y b i f m l", "Arcana", "Athletics"],
            max_height=5)

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
