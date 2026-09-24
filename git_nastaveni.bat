@echo off
:: Nastavení kódování UTF-8, aby se správně zobrazovala čeština
chcp 65001 > nul

title Nastavení Git Identity pro Školní PC
echo === Nastavení identity pro Git ===
echo.

set /p git_name="Zadejte vase cele jmeno: "
set /p git_email="Zadejte vas e-mail: "

echo.
echo Nastavuji Git proměnné a oprávnění...

:: 1. Obejití konfigurace přes proměnné prostředí
set GIT_AUTHOR_NAME=%git_name%
set GIT_AUTHOR_EMAIL=%git_email%
set GIT_COMMITTER_NAME=%git_name%
set GIT_COMMITTER_EMAIL=%git_email%

:: 2. Přesměrování domovské složky Gitu na lokální disk C: (vyřeší fatal chyby)
set HOME=C:\Users\%USERNAME%

:: 3. Automatické schválení aktuální složky (včetně síťové) pro Git
git config --global --add safe.directory "*" >nul 2>&1

echo.
echo === Hotovo! Identita je aktivní v tomto okně ===
echo Jméno:  %GIT_AUTHOR_NAME%
echo E-mail: %GIT_AUTHOR_EMAIL%
echo.
echo Nyní můžete v tomto okně normálně pracovat s Git.
echo.
cmd /k
