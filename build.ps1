pyinstaller  `
-w `
--onefile `
--add-data "./images;images" `
--add-data "./SQL;SQL" `
--name "password-manager" `
--distpath "./win32" `
'main.py'