# pip boilerplate

How do you publish this shit?

1. Change the git remote for this repo, so you don't overwrite the boilerplate.
2. Rename the `my_module` folder to whatever you want, and put your module there.
3. Make sure `__init__.py` contains everything you want to export.
4. Edit `setup.py`; replace the `name='my_module'` with whatever your module name is, then edit description, etc.
5. `bash release.sh` to release; version stuff is included in that script.

Good luck!
