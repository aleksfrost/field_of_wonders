# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ui_main.py'],
    pathex=['E:\\Python\\field_of_wonders\\game'],
    binaries=[('games.py', '.'), ('drum.py', '.'), ('main_game.py', '.'), ('prises.py', '.'), ('ui_login.py', '.'), ('ui_message.py', '.'), ('ui_stats.py', '.'), ('ui_yes_no_message.py', '.'), ('users.py', '.'), ('words.py', '.'), ('make_path.py', '.')],
    datas=[('drum.gif', '.'), ('fow.ico', '.'), ('wha.jpg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ui_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ui_main',
)
