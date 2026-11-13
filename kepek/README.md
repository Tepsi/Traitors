# Illusztrációk

Ide kerülnek a fejezetekhez tartozó illusztrációk promptjai és az elkészült képek. A képeket a szöveg kész állapotában szerkesztjük a fejezetekbe (a munkamód 4. lépésénél), addig csak ebben a mappában vannak.

## Elnevezés

`FF-SS-cim.md` a prompt, mellette ugyanezzel a névvel `.png` a kész kép. `FF` a fejezet sorszáma, `SS` a kép sorszáma a fejezeten belül.

## Hogyan épülnek a promptok

Minden prompt rögzíti: a kameraállást, az előteret, a középteret és a hátteret, a bal és jobb oldalt (mindig a néző szemszögéből), azt, hogy ki hol ül vagy áll, merre néz, és milyen irányba állnak a székek. A végén egy `DO NOT` sor felsorolja, amit a generátor ne tegyen. A promptok szándékosan hosszúak.

A helyszínek és a ruhák rögzített leírása a `helyszinek-es-szereplok.md` fájlban van, minden prompt ezekből építkezik. Ha egy generátor mégis elrontja a térbeli elrendezést (például a székeket az asztalnak háttal rakja), írd át a promptot a következő módon: ismételd meg a hibás részt, és fogalmazd meg ellentétes irányban („the chairs face the table, the sitters face each other").

## Generátor: Microsoft Create

A képek a Microsoft Create (Designer) segítségével készülnek, amely elfogadja a hosszú promptokat és a valós személyek neveit. Ezért minden promptfájl egyetlen, teljes részletességű promptot tartalmaz, a szereplők nevével együtt. Kivétel a `01-03` kép, ahol az érintett vendég szándékosan névtelen és nem látszik. Ha van képarány-választó, válaszd a fekvő (3:2 vagy 16:9) formátumot.

## Közös stílus

Minden prompt ugyanazzal a mondattal indul, így a képek egységesek lesznek:

> Monochrome graphite pencil drawing on cream paper, hand-hatched, soft smudged shading, fine paper grain, soft vignette edges, ominous gothic mood.

Tippek az egységességhez:

- Ugyanazt a generátort használd az összes képhez, és kérj 3:2 fekvő formátumot.
- Ha a generátor színt vagy fotót ad, tedd a prompt elejére: „black and white only, pencil on paper, not a photo".
- Negatív prompt, ha támogatja: `color, watercolor, photograph, 3D render, cartoon, anime, text, caption, signature, watermark`.
- Olvasható feliratot a generátorok rosszul írnak, ezért a promptok szándékosan olvashatatlan feliratot kérnek.
- Ha a generátor mégis elutasít egy nevet, cseréld a nevet korhű ruhaleírásra („a man in a 1950s dark suit and tie"), és a jellegzetes mozdulatot hagyd benne. A mozdulat a szereplő modorát hordozza, az arc felismerhetősége nem fontos.
- A szereplőket méltósággal ábrázold, karikatúra nélkül. A könyv humora a szövegben van, a képek komolyak.

## Képek

| Fájl | Kapcsolódó mondat | Kész |
|------|-------------------|------|
| `01-01-holdvari-kastely` | „A Holdvári-kastély a dombtetőn állt…" | rajz kész (vagy generátorral) |
| `01-02-a-jatekmester-az-erkelyen` | „…az erkélyen egyetlen fénysugár villant fel…" | |
| `01-03-a-hideg-ujj` | „Aztán hideg ujj érintette a vállát…" | |
| `01-04-a-konklave` | „A gyertya lángja meghajolt…" | |
| `02-01-az-elporladt-nevtabla` | „…a betűk szélei elporladtak…" | |
| `02-02-a-labirintus-bejarata` | „A bejáratnál kőív állt…" | |
| `02-03-bud-spencer-atmegy-a-soveny-falon` | „A tiszafa először nem engedett, aztán mégis." | |
| `02-04-latabar-a-kuszobon` | „A küszöbön megbotlott…" | |
| `03-01-a-csend-szalonja` | „A terem közepén hatalmas álló óra állt…" | |
| `03-02-mercury-tenyere` | „A ceruzával írt név már nem látszott…" | |
| `03-03-psota-iren-a-pajzzsal` | „…mintha kígyót fogna." | |
| `04-01-a-lanc` | „Így állt fel a lánc." | kész, beszerkesztve |
| `04-02-a-lepcson` | „A lába megcsúszott." | kész, beszerkesztve |
| `04-03-bessenyei-felall` | „Engedjék meg, hogy beszéljek." | kész, beszerkesztve |
| `05-01-a-nyugati-galeria` | „A padlója fekete és fehér márványlapokból állt, szabálytalan mintában…" | kész, beszerkesztve |
| `05-02-brando-a-vakon` | „Brando kötötte be a szemét, aztán hosszasan állt…" | kész, beszerkesztve |
| `05-03-agatha-helye` | „– Agatha helye – mondta Welles halkan." | kész, beszerkesztve |
| `05-04-taylor-a-kuszoben` | „Taylor megigazította a karperecét, a küszöbön megállt, és hátrafordult." | kész, beszerkesztve |
| `06-01-a-merleg` | „A terem közepén egy sárgaréz mérleg állt, két serpenyővel, akkora, hogy egy ember is elfért volna benne." | kész, beszerkesztve |
| `06-02-hitchcock-bucsuja` | „Hölgyeim és uraim: áruló vagyok." | kész, beszerkesztve |
| `06-03-a-fekete-lap` | „A tölgyajtó kinyílt, és egy csuklyás alak lépett a kőasztalhoz, a kezében a fekete lappal." | kész, beszerkesztve |
| `07-01-a-kapolna` | „Négy pad volt benne, szorosan egymás mellett, egy keskeny, magas ablak, amelyen át a tél színtelen fénye csak egyetlen sávban érte el a padlót, és egy vaskos oltárasztal, amelyen négy vastag gyertya égett, mindegyik ugyanolyan magasságú." | kész, beszerkesztve |
| `07-02-mercury-kivalt` | „Maria Callast váltom ki." | kész, beszerkesztve |
| `07-03-callas-a-kuszoben` | „Nem kértem, hogy fizessen értem valaki." | kész, beszerkesztve |
| `07-04-kabos-felall` | „Kabos felállt. A térde meginogott, de Puskás kinyújtotta a kezét, és megtartotta a könyökét." | kész, beszerkesztve |
| `08-01-a-nevek-terme` | „A terem közepén egy szürke bársonnyal letakart asztal állt, rajta egy urna, két homokóra és egy pecsétes láda, amelynek a tetején két fekete boríték feküdt egymás mellett, az urnától távol, mintha nem tartoznának a többi közé." | kész, beszerkesztve |
| `08-02-einstein-felall` | „Einstein volt az, aki felállt." | kész, beszerkesztve |
| `08-03-brando-a-kovon` | „Brando lecsúszott a székről a padlóra, és ott ült a kövön, az arcát a tenyerébe temetve, és nevetett és sírt egyszerre, előbb hangtalanul, a vállát rázva, aztán hangosan, megkönnyebbülten." | kész, beszerkesztve |
| `08-04-az-ures-szek` | „A gyertya lángja, amely tegnap még egyenesen égett, most az üres szék felé hajlott, mintha a közelében keresne valakit, és az asztal lapján nem feküdt semmi, sem szürke lap, sem fekete, csak a viasz kis, kihűlt cseppjei, ahol tegnap még valaki az ujját tartotta." | kész, beszerkesztve |
| `09-01-a-tukorterem` | „A terem közepén kőpárkány állt, a tetején sárgaréz láda, két tenyérnyi, keskeny réssel a fedelén." | |
| `09-02-brando-a-kapu-elott` | „A Kapu elé lépett, a kezét a zsebébe dugta, és sokáig csak állt ott, a fekete ajtóval szemközt, mintha a szavakat kellene megtalálnia." | |
| `09-03-zsazsa-es-a-fuzet` | „A füzetet az asztalra tette, és az ujja egy üres oldalra tévedt, aztán megállt." | |
