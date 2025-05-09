#!/bin/bash

if [ "$EUID" -ne 0 ]; then
  echo "Запустите скрипт с sudo для системной установки или без sudo для локальной."
fi

if [ "$EUID" -eq 0 ]; then
  DESKTOP_DIR="/usr/share/applications"
  MIME_DIR="/usr/share/mime/packages"
else
  DESKTOP_DIR="$HOME/.local/share/applications"
  MIME_DIR="$HOME/.local/share/mime/packages"
fi

mkdir -p "$DESKTOP_DIR" "$MIME_DIR"

cat << EOF > "$DESKTOP_DIR/rupython.desktop"
[Desktop Entry]
Name=Исполнитель кода Русского Питона
Exec=python3 -m rupython %F
Type=Application
Terminal=true
MimeType=application/x-rupython;
NoDisplay=true
EOF

cat << EOF > "$MIME_DIR/rupython.xml"
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/x-rupython">
    <comment>Код на Русском Питоне</comment>
    <glob pattern="*.крп"/>
  </mime-type>
</mime-info>
EOF

if [ "$EUID" -eq 0 ]; then
  update-mime-database /usr/share/mime
else
  update-mime-database "$HOME/.local/share/mime"
fi

xdg-mime default rupython.desktop application/x-rupython

if [ "$(xdg-mime query default text/plain)" = "rupython.desktop" ]; then
  xdg-mime default gedit.desktop text/plain || xdg-mime default xed.desktop text/plain
fi

update-desktop-database "$DESKTOP_DIR"

echo "Выполнено."
