# Árulók – Halálos kastély: munkakönyvtár

Magyar nyelvű fikciós sorozat. A szabályokat, a hangnemet és a határokat lásd: `projekt/projekt-utasitasok.md`, a szereplők modorát: `projekt/stilusjegyzet.md`, a teendőket: `projekt/teendok.md`.

## Felépítés
- `fejezetek/`: a megjelent fejezetek (`NN-cim.md`), publikusak.
- `projekt/`: nyilvános háttéranyag.
- `privat/`: helyi, git által figyelmen kívül hagyott mappa. Itt van a titkos terv (`titkos-terv.md`), a feliratok (`*.srt`), a feliratokból készült jegyzetek és a szerkesztői javaslatok. Spoilert tartalmaz.

## Szabályok
- A `privat/` tartalmát soha ne commitold, ne idézd a nyilvános fájlokban, és ne szivárogtasd ki az olvasói szövegben. Commit előtt nézd meg a `git status` kimenetét.
- Új fejezetnél ellenőrizd a szöveget a `privat/titkos-terv.md` ellen (fair play nyomok, ki mikor esik ki).
- A fejezetek gondolatjele az en-dash (–).
- A tévéműsor nevét és logóját nem használjuk, a Játékmester Szerafin Barnabás.

## Munkamód új fejezethez (tokentakarékos, lépésenként)
A felhasználó ingyenes Claude-ot használ, ezért kevés a token. Ezért: ne olvasd újra a feliratokat és a már megírt fejezeteket, csak amit az adott lépés igényel. Kis módosításhoz Edit-et használj, ne írd újra a teljes fájlt.

A repó **nyilvános**, ezért a `temporary/` mappába és a commit üzenetekbe csak olvasói szöveg és spoilermentes haladási jegyzet kerülhet. A vázlat és a titkos terv módosításai nem.

A titkos terv, a vázlatok és a feliratok jegyzetei a claude.ai Projectben vannak (`claude/titkos-terv.md`, `claude/jegyzet-*.md`), nem a repóban. Felhőmunkamenetben a `privat/` mappa nincs meg: a Projects eszközzel (`project_search`, `project_read`, `project_write`) érd el őket.

### Lépések
1. **Vázlat.** Dolgozd ki a fejezet vázlatát. Ha kell, módosítsd a titkos tervet és a többi dokumentációt. A vázlatot és a terv módosításait a Projectbe mentsd (`claude/NN-vazlat.md`, `claude/titkos-terv.md`), ne GitHubra. Mutasd meg a felhasználónak, mielőtt írni kezdesz, ha a vázlat új döntést igényel.
2. **Részenkénti írás.** A fejezetet részenként írd a `temporary/NN-cim.md` fájlba. Minden rész után commitold és pushold. A `temporary/allapot.md` spoilermentesen jelzi, hol tartunk (melyik rész kész, mi jön következőként, néhány szóban), hogy új beszélgetésben onnan lehessen folytatni.
3. **Átolvasás.** Ha a fejezet kész, olvasd át egyszer, és javítsd a következetlenségeket, a nyelvtani hibákat és a magyartalan mondatokat (Edit-tel). Ellenőrizd a szöveget a titkos terv megfelelő részével (fair play nyomok, ki esik ki).
4. **Lezárás.** Mentsd a kész fejezetet a `fejezetek/` mappába (`NN-cim.md`), frissítsd a `README.md` fejezettáblázatát és a `projekt/teendok.md`-t. A módosult privát jegyzeteket (titkos terv stb.) a Projectben frissítsd. Végül töröld a `temporary/` mappát (`git rm -r temporary`), és commitold, pushold.

### Commit
Minden commit üzenete a `Co-Authored-By` és a `Claude-Session` sorokkal végződik, ahogy a környezet előírja. Commit előtt nézd meg a `git status` kimenetét, `privat/` vagy jegyzet ne kerüljön bele.
