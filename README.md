# MPDF
## _Mob Proto Data Filler_
[![Release Package](https://github.com/icon-project/icon-release/workflows/Release%20packages/badge.svg?event=workflow_dispatch)](https://github.com/Owsap/MPDF/releases/tag/V1)

[![DEMO](https://img.youtube.com/vi/oqFcJW1GACE/maxresdefault.jpg)](https://youtu.be/oqFcJW1GACE)

This tool fills in missing values from extracted tables from official clients, these values such as gold, skills and other values are important for the final complete functioning of the table.
Below is a list of the columns the reference table will replace with your full table.
| Column | Description |
| ------ | ------ |
| GoldMin | Minimum Gold |
| GoldMax | Maximum Gold |
| ResurrectionVnum | Resurrection Virtual Number |
| PolymorphItem | Polymorph Item |
| SkillLevel0 | Skill Level 0
| SkillVnum0 | Skill Virtual Number 0
| SkillLevel1 | Skill Level 1
| SkillVnum1 | Skill Virtual Number 1
| SkillLevel2 | Skill Level 2
| SkillVnum2 | Skill Virtual Number 2
| SkillLevel3 | Skill Level 3
| SkillVnum3 | Skill Virtual Number 3
| SkillLevel4 | Skill Level 4
| SkillVnum4 | Skill Virtual Number 4

The reference values that will replace the fields of your table are from the official proto of 2014, as this table is a little old you can expand the file to your comfort.

## Features
- Multiple support for different types of tables that can be enabled in the `config.ini` file.
- Automatically fills null fields with `0`.
- Simple script that looks for all files in `monster2` folder that contain skills.

## Configuration
The `config.ini` file allows the tool to correctly read certain table columns.
Please note that **enabled columns must be in the correct order** as the official column.
```ini
[TABLE_STRUCTURE]
; ScalePct
MOB_SCALE = 0
; ResistClaw, ResistBleeding
WOLFMAN_CHARACTER = 0
; AttElec, AttFire, AttIce, AttWind, AttEarth
ELEMENTS = 0
```
For example, if your table contains columns like this: `Vnum	Name	Rank	Type	BattleType	Level	ScalePct	Size...` then you need to enable `MOB_SCALE`.
If your table contains columns with *Wolfman* that look like this, `...	ResistBow	ResistClaw	ResistFire	ResistElect	ResistMagic	ResistWind	ResistPoison	ResistBleeding	...` then you have to enable `WOLFMAN_CHARACTER`.
And continuously if you enable the `ELEMENTS` columns.

## Search Script
The script `find_special_attacks.py` makes it easier to find all the monsters that contain skills, this will help expand the reference file with new entries.
Using it is very simple, paste the script outside your client's `monster2` folder.
> There is currently no way to know the exact skill level and vnum for new entries (monsters) that are not in the reference file, but considering the monster's skill type, a bit of logic can help.
